from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Comment_movie
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer
from rest_framework import status
# Create your views here.


# @api_view(['GET', 'POST'])
@api_view(['GET'])
def index(request):
    # if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    # else:
    #     if request.user.is_authenticated:                        
    #         serializer = MovieSerializer(data=request.data)
    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save(user=request.user)
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['GET', 'DELETE', 'PATCH'])
@api_view(['GET'])
def detail(request, movie_id):    
    movie = get_object_or_404(Movie, id=movie_id)
    # if request.method == 'GET':
    serializer = MovieSerializer(movie)                    
    return Response(serializer.data)
    # else:
    #     if request.user.is_authenticated:            
    #         if request.user.is_superuser:
    #             if request.method == 'PATCH':
    #                 serializer = MovieSerializer(data=request.data)
    #                 if serializer.is_valid():
    #                     serializer.save()
    #                     return Response(serializer.data)
    #                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #             else:
    #                 article.delete()
    #                 return Response(status=status.HTTP_204_NO_CONTENT)            
    #         return Response(status=status.HTTP_403_FORBIDDEN)
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)



# 영화 평점, 댓글 
@api_view(['GET', 'POST'])
def review(request, movie_pk):      
    movie = get_object_or_404(Movie, pk=movie_pk)        
    if request.method == 'GET':
        print('요청옴')
        reviews = Comment_movie.objects.filter(movie_id=movie_pk)         
        serializer = ReviewListSerializer(reviews, many=True)        
        return Response(serializer.data)
    elif request.method == 'POST':
        print('=======================')
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):            
                serializer.save(user=request.user, movie=movie)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_change(request, movie_pk, review_pk):      
    movie = get_object_or_404(Movie, pk=movie_pk)       
    review = get_object_or_404(Comment_movie, pk=review_pk)       
    if request.user == review.user:
        if request.method == 'PUT':
            serializer = ReviewSerializer(instance=review, data=request.data)                
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)            
    return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
def check_review(request, movie_pk, review_pk):      
    review = get_object_or_404(Comment_movie, pk=review_pk)       
    if review.user==request.user:
        return Response({true})
    return Response(status=status.HTTP_403_FORBIDDEN)