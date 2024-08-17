from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from posts.models import Post
from posts.serializers import PostSerializer


# Create your views here.
class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
