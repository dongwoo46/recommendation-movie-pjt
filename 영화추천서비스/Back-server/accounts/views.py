from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer,CommentSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .models import *


@api_view(['GET', 'POST'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    # 내가 보고있는 프로필 유저
    profile_user = get_object_or_404(get_user_model(), username=username)
    me = request.user

    print(f'프로필 유저 : ', profile_user)
    print(f'나 : ', me)
    if me != profile_user:
        if me in profile_user.followers.all():
            profile_user.followers.remove(me)
        else:
            profile_user.followers.add(me)
    
    serializer = UserSerializer(profile_user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followers_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    followers = user.followers.all()
    serializer = UserSerializer(followers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followings_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    followings = user.followings.all()
    serializer = UserSerializer(followings, many=True)
    return Response(serializer.data)

    
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def profile_comment(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        comments = person.comments.all()
        serializer = CommentSerializer(comments, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=person)
            return Response(serializer.data, status=status.HTTP_201_CREATED)