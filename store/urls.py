# from django.contrib import admin
from django.urls import path
from .views import home,signup,login
from .views .login import logout
from .views.cart import Cart
# from .views.order import Order
from .views .checkout import CheckOut
# from django.urls import path


urlpatterns = [
    path('', home.index.as_view(), name="homepage"),
    path('signup', signup.signup.as_view(),name="signup"),
    path('login', login.login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('cart', Cart.as_view(), name="cart"),
    path('checkout', CheckOut.as_view(), name="checkout"),

]