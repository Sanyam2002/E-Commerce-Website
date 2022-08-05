from django.contrib import admin
from .models import(
    Customer,
    Product,
    Cart,
    OrderPlaced,
    catcart
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state','phone']

@admin.register(Product)
class ProductModelAdmin (admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price','discounted_price', 'description', 'brand', 'category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity','catego']

@admin.register(catcart)
class catcartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','categ']

@admin.register (OrderPlaced)   
class OrderPlacedModelAdmin(admin.ModelAdmin): 
    list_display = ['id', 'user', 'customer', 'product','quantity', 'ordered_date', 'status']