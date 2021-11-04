from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    class Meta:
        model = Post
        fields = ['id', 'author','title','content','created_date','published_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name="blog:post-detail", read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']



