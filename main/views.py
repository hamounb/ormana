from django.shortcuts import render
from .models import ContactUsModel
from .forms import *
from django import views
from django.http import HttpResponseRedirect

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
    

class ProductsUseView(views.View):

    def get(self, request):
        return render(request, "main/products-use.html")
    

class AboutUsView(views.View):

    def get(self, request):
        return render(request, "main/about-us.html")
    

class ContactUsSubmitView(views.View):

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            mobile = form.cleaned_data.get("mobile")
            text = form.cleaned_data.get("text")
            new_contact = ContactUsModel(
                name=name,
                mobile=mobile,
                text=text,
            )
            new_contact.save()
            context = {
                name:name,
                mobile:mobile,
                text:text,
            }
            return render(request, "main/contact-us-submit.html", context)
        referer = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(referer)