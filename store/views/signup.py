from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer


class signup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstName')
        last_name = postData.get('lastName')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation
        value = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
        }

        error_message = None
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password
        )
        error_message = self.validatecustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validatecustomer(self, customer):
        error_message = None

        if not customer.first_name:
            error_message = "Enter Your Name "
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 Chracter Long"
        elif not customer.last_name:
            error_message = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_message = "last Name Must be 4 chracter long"
        elif not customer.phone:
            error_message = "Phone Number Required"
        elif len(customer.phone) < 10:
            error_message = "Please Enter a valid Number"
        elif len(customer.email) < 6:
            error_message = "Email Must be 6 Chracter Long"
        elif len(customer.password) < 6:
            error_message = "Password Must Be 6 Chracter Long"
        elif customer.isExists():
            error_message = "Email is Already register"
            return error_message
