from django.contrib import admin

from .models import Gem, Client, Order


class GemAdmin(admin.ModelAdmin):

        list_display = ('name', )
        search_fields = ('name', )


class ClientAdmin(admin.ModelAdmin):

    list_display = ('username', 'spent_money')
    search_fields = ('username', )


class OrderAdmin(admin.ModelAdmin):

        list_display = ('customer', 'item', 'total', 'quantity')
        search_fields = ('customer','item')


admin.site.register(Gem, GemAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
