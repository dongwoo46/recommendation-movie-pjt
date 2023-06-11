
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import FreeBoardListSerializer, FreeBoardSerializer,  FreeCommentSerializer, LoveBoardListSerializer, LoveBoardSerializer, LoveCommentSerializer, SecretBoardListSerializer, SecretBoardSerializer, SecretCommentSerializer, FriendBoardListSerializer, FriendBoardSerializer, FriendCommentSerializer
from .models import FreeBoard, FreeComment, LoveBoard, LoveComment, SecretBoard, SecretComment, FriendBoard, FriendComment


# 자유게시판
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def FreeBoards_list(request):
    if request.method == 'GET':
        freeboards = FreeBoard.objects.all()
        serializer = FreeBoardListSerializer(freeboards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FreeBoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'DELETE', 'PUT'])
def FreeBoard_detail(request, freeboard_pk):
    freeboard = get_object_or_404(FreeBoard, pk=freeboard_pk)

    if request.method == 'GET':
        serializer = FreeBoardSerializer(freeboard)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        freeboard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = FreeBoardSerializer(freeboard, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def FreeComments_list(request, freeboard_pk):
    freeboard = get_object_or_404(FreeBoard, pk=freeboard_pk)
    if request.method == 'GET':
        freecomments = freeboard.freecomments.all()
        serializer = FreeCommentSerializer(freecomments, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FreeCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(freeboard=freeboard, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def FreeComment_detail(request, freeboard_pk, freecomment_pk):
    freecomment = get_object_or_404(FreeComment, pk=freecomment_pk)

    if request.method == 'GET':
        serializer = FreeCommentSerializer(freecomment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        freecomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = FreeCommentSerializer(freecomment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def FreeComment_create(request, freeboard_pk):
    freeboard = get_object_or_404(FreeBoard, pk=freeboard_pk)
    serializer = FreeCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(freeboard=freeboard, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 연애게시판
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def LoveBoards_list(request):
    if request.method == 'GET':
        loveboards = LoveBoard.objects.all()
        serializer = LoveBoardListSerializer(loveboards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoveBoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'DELETE', 'PUT'])
def LoveBoard_detail(request, loveboard_pk):
    loveboard = get_object_or_404(LoveBoard, pk=loveboard_pk)

    if request.method == 'GET':
        serializer = LoveBoardSerializer(loveboard)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        loveboard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = LoveBoardSerializer(loveboard, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def LoveComments_list(request, loveboard_pk):
    loveboard = get_object_or_404(LoveBoard, pk=loveboard_pk)
    if request.method == 'GET':
        lovecomments = loveboard.lovecomments.all()
        serializer = LoveCommentSerializer(lovecomments, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LoveCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(loveboard=loveboard, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def LoveComment_detail(request, loveboard_pk, lovecomment_pk):
    lovecomment = get_object_or_404(LoveComment, pk=lovecomment_pk)

    if request.method == 'GET':
        serializer = LoveCommentSerializer(lovecomment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        lovecomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = LoveCommentSerializer(lovecomment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def LoveComment_create(request, loveboard_pk):
    loveboard = get_object_or_404(LoveBoard, pk=loveboard_pk)
    serializer = LoveCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(loveboard=loveboard, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 비밀게시판
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def SecretBoards_list(request):
    if request.method == 'GET':
        secretboards = SecretBoard.objects.all()
        serializer = SecretBoardListSerializer(secretboards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SecretBoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'DELETE', 'PUT'])
def SecretBoard_detail(request, secretboard_pk):
    secretboard = get_object_or_404(SecretBoard, pk=secretboard_pk)

    if request.method == 'GET':
        serializer = SecretBoardSerializer(secretboard)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        secretboard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = SecretBoardSerializer(secretboard, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def SecretComments_list(request, secretboard_pk):
    secretboard = get_object_or_404(SecretBoard, pk=secretboard_pk)
    if request.method == 'GET':
        secretcomments = secretboard.secretcomments.all()
        serializer = SecretCommentSerializer(secretcomments, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SecretCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(secretboard=secretboard, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def SecretComment_detail(request, secretboard_pk, secretcomment_pk):
    secretcomment = get_object_or_404(SecretComment, pk=secretcomment_pk)

    if request.method == 'GET':
        serializer = SecretCommentSerializer(secretcomment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        secretcomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = SecretCommentSerializer(secretcomment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SecretComment_create(request, secretboard_pk):
    secretboard = get_object_or_404(SecretBoard, pk=secretboard_pk)
    serializer = SecretCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(secretboard=secretboard, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 친구게시판
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def FriendBoards_list(request):
    if request.method == 'GET':
        friendboards = FriendBoard.objects.all()
        serializer = FriendBoardListSerializer(friendboards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FriendBoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'DELETE', 'PUT'])
def FriendBoard_detail(request, friendboard_pk):
    friendboard = get_object_or_404(FriendBoard, pk=friendboard_pk)

    if request.method == 'GET':
        serializer = FriendBoardSerializer(friendboard)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        friendboard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = FriendBoardSerializer(friendboard, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def FriendComments_list(request, friendboard_pk):
    friendboard = get_object_or_404(FriendBoard, pk=friendboard_pk)
    if request.method == 'GET':
        friendcomments = friendboard.friendcomments.all()
        serializer = FriendCommentSerializer(friendcomments, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FriendCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(friendboard=friendboard, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def FriendComment_detail(request, friendboard_pk, friendcomment_pk):
    friendcomment = get_object_or_404(FriendComment, pk=friendcomment_pk)

    if request.method == 'GET':
        serializer = FriendCommentSerializer(friendcomment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        friendcomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = FriendCommentSerializer(friendcomment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def FriendComment_create(request, friendboard_pk):
    friendboard = get_object_or_404(FriendBoard, pk=friendboard_pk)
    serializer = FriendCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(friendboard=friendboard, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
