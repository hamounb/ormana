from django.shortcuts import render
from django import views

# Create your views here.

a = False

class IndexView(views.View):

    def get(self, request):
        if a:
            return render(request, "main/coming-soon.html")
        return render(request, "main/index.html")
    

class ProductsView(views.View):

    def get(self, request):
        return render(request, "main/products.html")
    

class AboutUsView(views.View):

    def get(self, request):
        return render(request, "main/about-us.html")