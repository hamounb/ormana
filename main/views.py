from django.shortcuts import render
from django import views

# Create your views here.

a = True

class IndexView(views.View):

    def get(self, request):
        if a:
            return render(request, "main/coming-soon.html")
        return render(request, "main/index.html")