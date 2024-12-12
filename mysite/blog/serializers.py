# blog/serializers.py
from rest_framework import serializers
from .models import Blog, Comment, LikeBlog
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(WritableNestedModelSerializer):
    blog =  serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())
    class Meta:
        model = Comment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id']

class LikeBlogCreateSerializer(WritableNestedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())

    class Meta:
        model = LikeBlog
        fields = '__all__'

class LikeBlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    blog = BlogSerializer(read_only=True)

    class Meta:
        model = LikeBlog
        fields = '__all__'
