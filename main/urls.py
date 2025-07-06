from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("products/", ProductsView.as_view(), name="products"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
]