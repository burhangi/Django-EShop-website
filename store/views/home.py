from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

class index(View):
    # def post(self, request):
    #     product_id = request.POST.get('product')
    #     if not product_id:
    #         return redirect('homepage')
    #
    #     cart = request.session.get('cart', {})
    #     cart[product_id] = cart.get(product_id, 0) + 1
    #     request.session['cart'] = cart
    #
    #     return redirect('homepage')

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})

        if cart:
            quantity = cart.get(product)
            if quantity is not None:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {product: 1}

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self,request):

        products = None
        categories = Category.get_all_Categories()
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_all_product_by_category_id(category_id)
        else:
            products = Product.get_all_product()

        data = {'products': products, 'categories': categories}
        print('you are :', request.session.get('email'))
        return render(request, 'index.html', data)


# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$390000$oB7wjcyaTNU8MiLi4NrXi6$Rq5B77MsP5erjJE0nUDbuvtcDfmU49yoyUAy2KvymXg='))

