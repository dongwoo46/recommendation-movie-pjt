from django.shortcuts import render, redirect
import requests
import json, os
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import update_session_auth_hash, get_user_model
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review
from django.views.decorators.http import require_http_methods, require_POST


# API_KEY = os.environ.get('MOIVE_API_KEY')
API_KEY = 'a93f9fd4dffec2c4dc9eaa9c115bf613'

# Create your views here.

@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        action = []
        comedy = []
        family = []
        romance= []
        drama= []
        horror= []
        thriller= []
        fantasy= []
        ani= []
        document= []
        SF= []
        music= []

        for i in range(1, 20):   
            url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page={i}'
            response = requests.get(url)

            if response.status_code == 200:
                movies = response.json()
                
                for movie_data in movies['results']:
                    
                    movie = Movie(
                        title=movie_data['title'],
                        genre=movie_data['genre_ids'],
                        poster_path=movie_data['poster_path'],
                        vote_average=movie_data['vote_average'],
                        id=movie_data['id'],
                    )
                    movie.save()
                    movie_serializer = MovieSerializer(movie)
                    serialized_movie = movie_serializer.data
                    serialized_movie['Movie_pk'] = movie.pk

                    
                    for genre in movie_data['genre_ids']:
                        if genre == 28:
                            action.append(serialized_movie)
                        elif genre == 35:
                            comedy.append(serialized_movie)
                        elif genre == 10751:
                            family.append(serialized_movie)
                        elif genre == 10749:
                            romance.append(serialized_movie)
                        elif genre == 18:
                            drama.append(serialized_movie)
                        elif genre == 27:
                            horror.append(serialized_movie)
                        elif genre == 53:
                            thriller.append(serialized_movie)
                        # elif genre == 53 or genre == 80:
                        #     thriller.append(serialized_movie)
                        elif genre == 14:
                            fantasy.append(serialized_movie)
                        elif genre == 16:
                            ani.append(serialized_movie)
                        elif genre == 99:
                            document.append(serialized_movie)
                        # elif genre == 99 or genre == 36:
                        #     document.append(serialized_movie)
                        elif genre == 878:
                            SF.append(serialized_movie)         
                        elif genre == 10402:
                            music.append(serialized_movie)
                   
                context = {
                    'action' : action,
                    'comedy': comedy,
                    'family':family,
                    'romance': romance,
                    'drama': drama,
                    'horror': horror,
                    'thriller': thriller,
                    'fantasy': fantasy,
                    'ani': ani,
                    'document': document,
                    'SF': SF,
                    'music': music,
                }

            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        return Response(context, status=status.HTTP_200_OK) 

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def reviews_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def review_delete(request, review_pk):
    if request.method == 'DELETE':
        review = get_object_or_404(Review, pk=review_pk)
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
