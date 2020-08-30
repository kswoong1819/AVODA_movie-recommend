from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article, Comment_article
from movies.models import Movie
from .serializers import ArticleSerializer, ArticleListSerializer, CommentListSerializer, CommentSerializer

from rest_framework import status


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def index(request):
    # get은 2번째 인자에 헤더 값 넣어주고    
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        # post는 2번째가 body, 3번째가 헤더
        serializer = ArticleSerializer(data=request.data)    
        if serializer.is_valid(raise_exception=True):            
            # serializer.data.user = request.user            
            serializer.save(user = request.user)                   
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['GET', 'DELETE', 'PUT'])
# 여기 DELETE랑 PATCH 인자들 알아놓고 제대로 된 axios 보내기!!!
@permission_classes([IsAuthenticated])
def detail(request, article_pk):    
    article = get_object_or_404(Article, pk=article_pk)        
    if request.method == 'GET':
        serializer = ArticleSerializer(article)        
        return Response(serializer.data)
    else:
        if request.user == article.user:
            if request.method == 'PUT':                                                        
                serializer = ArticleSerializer(instance=article, data=request.data)                
                if serializer.is_valid():
                    serializer.save()
                    # return Response(serializer.data)
                    return Response({'message':'수정됨'})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                article.delete()
                # return Response(status=status.HTTP_204_NO_CONTENT)            
                return Response({'message':'삭제됨'})
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment(request, article_pk):      
    article = get_object_or_404(Article, pk=article_pk)        
    if request.method == 'GET':
        comments = Comment_article.objects.filter(article_id=article_pk)         
        serializer = CommentListSerializer(comments, many=True)        
        return Response(serializer.data)
    elif request.method == 'POST':        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):            
            serializer.save(user=request.user, article=article)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                


@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_change(request, article_pk, comment_pk):  
    print('댓글 바꿔라')    
    print(request.user)
    article = get_object_or_404(Article, pk=article_pk)       
    comment = get_object_or_404(Comment_article, pk=comment_pk)       
    if request.user == comment.user:
        if request.method == 'PUT':
            serializer = CommentSerializer(instance=comment, data=request.data)                
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)            
    return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
def check_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)       
    if article.user==request.user:
        return Response({true})
    return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
def check_comment(request, article_pk, comment_pk):  
    comment = get_object_or_404(Comment_article, pk=comment_pk)       
    if comment.user==request.user:
        return Response({true})
    return Response(status=status.HTTP_403_FORBIDDEN)