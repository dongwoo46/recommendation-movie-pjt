# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    # 자유게시판
    path('freeboard/', views.FreeBoards_list),
    path('freeboard/<int:freeboard_pk>/', views.FreeBoard_detail),
    path('freeboard/<int:freeboard_pk>/freecomment/', views.FreeComments_list),
    path('freeboard/<int:freeboard_pk>/freecomment/create/', views.FreeComment_create),
    path('freeboard/<int:freeboard_pk>/freecomment/<int:freecomment_pk>/', views.FreeComment_detail),

    # 연애게시판
    path('loveboard/', views.LoveBoards_list),
    path('loveboard/<int:loveboard_pk>/', views.LoveBoard_detail),
    path('loveboard/<int:loveboard_pk>/lovecomment/', views.LoveComments_list),
    path('loveboard/<int:loveboard_pk>/lovecomment/create/', views.LoveComment_create),
    path('loveboard/<int:loveboard_pk>/lovecomment/<int:lovecomment_pk>/', views.LoveComment_detail),

    # 비밀게시판
    path('secretboard/', views.SecretBoards_list),
    path('secretboard/<int:secretboard_pk>/', views.SecretBoard_detail),
    path('secretboard/<int:secretboard_pk>/secretcomment/', views.SecretComments_list),
    path('secretboard/<int:secretboard_pk>/secretcomment/create/', views.SecretComment_create),
    path('secretboard/<int:secretboard_pk>/secretcomment/<int:secretcomment_pk>/', views.SecretComment_detail),

    # 친구게시판
    path('friendboard/', views.FriendBoards_list),
    path('friendboard/<int:friendboard_pk>/', views.FriendBoard_detail),
    path('friendboard/<int:friendboard_pk>/friendcomment/', views.FriendComments_list),
    path('friendboard/<int:friendboard_pk>/friendcomment/create/', views.FriendComment_create),
    path('friendboard/<int:friendboard_pk>/friendcomment/<int:friendcomment_pk>/', views.FriendComment_detail),

]
