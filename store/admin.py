# from django.contrib import admin
# from .models.product import Product
# from .models.category import Category
# from .models.customer import Customer
# # Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Customer)
from django.contrib import admin
from .models.product import Product
from .models.category import Category
from.models.category import Category
from .models.customer import Customer
from .models.order import Order
# Register your models here.

class adminproduct(admin.ModelAdmin):
    list_display = ['name','price','category' ]

class admincategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product,adminproduct)
admin.site.register(Category,admincategory)
admin.site.register(Customer)
admin.site.register(Order)
