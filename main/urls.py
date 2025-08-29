from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("products/", ProductsView.as_view(), name="products"),
    path("products-use/", ProductsUseView.as_view(), name="products-use"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
    path("contact-us/submit/", ContactUsSubmitView.as_view(), name="contact-us-submit"),
]