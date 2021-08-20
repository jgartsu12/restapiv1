from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'description', 'updated-on', 'content', 'created-on', 'status']