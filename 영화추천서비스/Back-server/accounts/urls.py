from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<username>/', views.profile),
    path('<username>/comments/', views.profile_comment),

    
    # path('<username>/profileChange/', ImageUploadView.as_view()),
    path('<username>/follow/', views.follow),
    path('<username>/followers_list/', views.followers_list),
    path('<username>/followings_list/', views.followings_list),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

