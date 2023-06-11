from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer


# 단일 리뷰 정보
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'created_at', 'updated_at', 'user', )

# 전체 영화 정보
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','id')

# 단일 영화 정보
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'poster_path',
            'vote_average',
        )


