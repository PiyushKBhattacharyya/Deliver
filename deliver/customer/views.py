from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')
    
class Order(View):
    def get(self, request, *args, **kwargs):
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        main_course = MenuItem.objects.filter(category__name__contains='Main Course')

        context = {
            'appetizers' : appetizers,
            'main_course' : main_course,
        }

        return render(request, 'customer/order.html', context)
    
    def post(self, request, *args, **kwargs):