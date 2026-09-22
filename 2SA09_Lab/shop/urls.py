from django.urls import path
from shop import views

app_name = "shop"
urlpatterns = [
    path("products", views.product_list, name="product-list"),
    path("products/<int:product_id>", views.product_detail, name="product-detail"),
]