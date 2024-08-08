from django.contrib import admin
from django.urls import path, include

from olcha_shop.views import CategoryListView, GroupListView, ProductListView, CommentListView, \
    ImageListView, AttributeListView, CategoryDetailAPIView, ProductListAPIView, CategoryDetailAPIView, \
    ProductListAPIView, CategoryCreateView, GroupDetailAPIView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category-detail/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('category-create/', CategoryCreateView.as_view(), name='category-create'),
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('group/<slug:slug>/detail/', GroupDetailAPIView.as_view(), name='group-detail'),
    path('category/<slug:category_slug>/<slug:group_slug>/', ProductListAPIView.as_view(), name='product_list'),
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('images/', ImageListView.as_view(), name='image_list'),
    path('attributes/', AttributeListView.as_view(), name='attribute_list'),
]
