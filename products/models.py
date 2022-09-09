from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from extensions.utils import jalali_convertor

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:detail', args=[self.pk])

    def active_comments(self):
        return Comment.objects.filter(product=self, active=True)


class Comment(models.Model):
    PRODUCT_STARS = (
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Noraml'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    stars = models.CharField(max_length=20, choices=PRODUCT_STARS)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def j_datetime_created(self):
        return jalali_convertor(self.datetime_created)