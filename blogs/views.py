from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from blogs.serializers import BlogSerializer
from blogs.models import Blog

class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny,)

class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class =  BlogSerializer
    permission_classes = (permissions.AllowAny, )

class BlogCreateView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class =  BlogSerializer
    permission_classes = (permissions.IsAuthenticated, )

class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class =  BlogSerializer
    permission_classes = (permissions.IsAuthenticated, )

class BlogDeleteView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticated, )
