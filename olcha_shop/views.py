from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from olcha_shop.models import Category


# Create your views here.

class CategoryListView(APIView):
    def get(self, request):
        category_data = [
            {
                'ID': category.id,
                'title': category.title,
                'slug': category.slug,
                'image_url': category.image.url,
            }
            for category in Category.objects.all()
        ]
        return Response(category_data, status=status.HTTP_200_OK)

