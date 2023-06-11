from rest_framework import serializers
from .models import FreeBoard, FreeComment, LoveBoard, LoveComment, SecretBoard, SecretComment, FriendBoard, FriendComment
from accounts.serializers import UserSerializer

# 자유 게시판
class FreeBoardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FreeBoard
        fields = ('id', 'title', 'content',)
        

class FreeCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = FreeComment
        fields = '__all__'
        read_only_fields = ('freeboard', 'user', )


class FreeBoardSerializer(serializers.ModelSerializer):
    freecomments = FreeCommentSerializer(many=True, read_only=True)
    freecomments_count = serializers.IntegerField(source='freecomments.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = FreeBoard
        fields = '__all__'
        read_only_fields = ('user',)


# 연애 게시판
class LoveBoardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoveBoard
        fields = ('id', 'title', 'content',)
        

class LoveCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = LoveComment
        fields = '__all__'
        read_only_fields = ('loveboard', 'user', )


class LoveBoardSerializer(serializers.ModelSerializer):
    lovecomments = LoveCommentSerializer(many=True, read_only=True)
    lovecomments_count = serializers.IntegerField(source='lovecomments.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = LoveBoard
        fields = '__all__'
        read_only_fields = ('user',)


# 비밀 게시판
class SecretBoardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SecretBoard
        fields = ('id', 'title', 'content',)
        

class SecretCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = SecretComment
        fields = '__all__'
        read_only_fields = ('secretboard', 'user', )


class SecretBoardSerializer(serializers.ModelSerializer):
    secretcomments = SecretCommentSerializer(many=True, read_only=True)
    secretcomments_count = serializers.IntegerField(source='secretcomments.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = SecretBoard
        fields = '__all__'
        read_only_fields = ('user',)


# 친구 게시판
class FriendBoardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendBoard
        fields = ('id', 'title', 'content',)
        

class FriendCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = FriendComment
        fields = '__all__'
        read_only_fields = ('friendboard', 'user', )


class FriendBoardSerializer(serializers.ModelSerializer):
    friendcomments = FriendCommentSerializer(many=True, read_only=True)
    friendcomments_count = serializers.IntegerField(source='friendcomments.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = FriendBoard
        fields = '__all__'
        read_only_fields = ('user',)







