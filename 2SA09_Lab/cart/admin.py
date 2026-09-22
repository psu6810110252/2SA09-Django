from django.contrib import admin
from cart.models import CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "qty"]
    list_filter = ["user"]
    autocomplete_fields = ["product"]