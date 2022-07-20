import django_filters
from django.db import models
from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=128)
    price = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class AdFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )

    class Meta:
        model = Ad
        fields = ("title",)
