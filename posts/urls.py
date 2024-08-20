from django.urls import path

from posts.views import PostListView

urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post-list'),
]