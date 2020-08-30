from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, Comment_article

class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at')    


class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    article = ArticleSerializer() #여기야
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Comment_article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleSerializer(required=False) #여기야

    class Meta:
        model = Comment_article
        fields = '__all__'
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at')
