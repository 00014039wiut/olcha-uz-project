from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from olcha_shop.models import Category, Group, Product, Comment, Image, Attribute
from olcha_shop.serializers import CategorySerializer, ProductSerializer, CommentSerializer, ImageSerializer, \
    AttributeSerializer, GroupSerializer, LoginUserSerializer, UserRegisterSerializer


# Create your views here.

# class CategoryListAPIView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [permissions.IsAuthenticated]


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view()
# def category_list(request):
#     categories = Category.objects.all()
#     serializer = CategorySerializer(categories, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view()
# def category_detail(request, pk):
#     category = Category.objects.get(pk=pk)
#     serializer = CategorySerializer(category, many=False)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['POST'])
# def category_create(request):
#     serializer = CategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
class CategoryCreateView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
#
# class CategoriesListView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class GroupListView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GroupListAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'slug'


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [TokenAuthentication]

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        group_slug = self.kwargs['group_slug']
        queryset = Product.objects.filter(group__category__slug=category_slug, group__slug=group_slug)
        return queryset


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ImageListView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AttributeListView(generics.ListCreateAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    lookup_field = 'pk'


class UserLoginAPIView(APIView):
    def post(self, request, *args, **kargs):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                "username": {
                    "detail": "User Doesnot exist!"
                }
            }
            if User.objects.filter(username=request.data['username']).exists():
                user = User.objects.get(username=request.data['username'])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                    'token': token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterAPIView(APIView):
    def post(self, request, *args, **kargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'user': serializer.data,
                'token': Token.objects.get(user=User.objects.get(username=serializer.data['username'])).key
            }
            return Response(response, status=status.HTTP_200_OK)
        raise ValidationError(
            serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)
