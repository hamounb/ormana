from django.db import models

# Create your models here.

class ContactUsModel(models.Model):
    name = models.CharField(verbose_name="نام و نام خانوادگی", max_length=200)
    mobile = models.CharField(verbose_name="شماره تماس", max_length=11)
    text = models.TextField(verbose_name="پیام")
    created_date = models.DateTimeField(verbose_name="تاریخ ثبت", auto_now_add=True)

    class Meta:
        verbose_name = "پیغام"
        verbose_name_plural = "پیغام ها"

    def __str__(self):
        return f"{self.name} ({self.mobile})"