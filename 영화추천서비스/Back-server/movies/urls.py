from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index),
    path('<int:movie_pk>/', views.detail),
    path('<int:movie_pk>/reviews/', views.reviews_list),
    path('<int:review_pk>/reviews/delete/', views.review_delete),
    
]
