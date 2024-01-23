from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name="Наименование категории")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    title = models.CharField(max_length=255,verbose_name="Наименование")
    price = models.FloatField(max_length=15,verbose_name="Цена")
    code = models.CharField(max_length=100,verbose_name="Штрих код")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    date_added = models.DateTimeField(default=timezone.now) 
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='products')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

