from django.contrib import admin
from django.urls import path, include

from olcha_shop.views import CategoryListView, GroupListView, CategoriesListView, ProductListView, CommentListView, \
    ImageListView, AttributeListView, category_list, category_detail, category_create, CategoryCreateView, \
    CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('category-detail/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('category-create/', CategoryCreateView.as_view(), name='category-create'),
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('images/', ImageListView.as_view(), name='image_list'),
    path('attributes/', AttributeListView.as_view(), name='attribute_list'),
]
