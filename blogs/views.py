from rest_framework import viewsets
from rest_framework import permissions

from blogs.serializers import BlogSerializer
from .models import Blog

class BlogViewSet(viewsets.ModelViewSet):
    # api endpt allows companies to viewed || edited
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
