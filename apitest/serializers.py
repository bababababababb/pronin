from rest_framework import serializers

from .models import Client, Order, Gem


class GemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gem
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

    def get_gems(customer_name):
        top_customers = [_.get('username') for _ in Client.objects.all().order_by('-spent_money')[:5].values('username')]

        gems = []
        customer_gems = [_.get('item') for _ in Order.objects.filter(customer=customer_name).values('item')]
        for order in Order.objects.all().values('customer', 'item'):
            if order.get('customer') in top_customers and order.get('item') in customer_gems:
                gems.append(order.get('item'))

        needed_gems = []
        for gem in Gem.objects.all().values():
            if gem.get('name') in gems:
                needed_gems.append(gem.get('id'))

        return needed_gems

    def get_spent_money(customer_name):
        spent_money = 0
        for order in Order.objects.all().values():
            if order.get('customer') == customer_name:
                spent_money += order.get('total')
        return spent_money


class CsvUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'customer',
            'item',
            'total',
            'quantity',
            'date'
        )

    def create(self, validated_data):
        deals = Order.objects.all()
        customer_name = validated_data.get('customer')
        gem_name = validated_data.get('item')
        customers = [_.get('username') for _ in Client.objects.all().values('username')]

        if gem_name not in [gem.get('name') for gem in Gem.objects.all().values('name')]:
            Gem.objects.create(name=gem_name).save()

        if customer_name not in customers:
            created_customer = Client.objects.create(
                username=customer_name,
                spent_money=ClientSerializer.get_spent_money(customer_name),
            )
            created_customer.save()
            created_customer.gems.set(ClientSerializer.get_gems(customer_name))
        objects = [_ for _ in deals.values('customer', 'item', 'total', 'quantity', 'date')]
        if validated_data in objects:
            return None

        return Order.objects.create(**validated_data)


