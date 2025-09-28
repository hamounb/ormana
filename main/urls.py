from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("en/", IndexEnView.as_view(), name="index-en"),
    path("products/", ProductsView.as_view(), name="products"),
    path("en/products/", ProductsEnView.as_view(), name="products-en"),
    path("products-use/", ProductsUseView.as_view(), name="products-use"),
    path("en/products-use/", ProductsUseEnView.as_view(), name="products-use-en"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
    path("en/about-us/", AboutUsEnView.as_view(), name="about-us-en"),
    path("contact-us/submit/", ContactUsSubmitView.as_view(), name="contact-us-submit"),
]