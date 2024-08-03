from django.contrib import admin
from django.urls import path, include

from olcha_shop.views import CategoryListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
]
