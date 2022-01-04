from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from .views import UserSignupAPIView, UserLoginAPIView, UserAPIView, UserLogoutAPIView

urlpatterns = [
    path('api_signup/',UserSignupAPIView.as_view(),name='users_api_signup'),
    path('api_login/',UserLoginAPIView.as_view(),name='users_api_login'),
    path('api_logout/',UserLogoutAPIView.as_view(),name='users_api_logout'),
    path('api_user/',UserAPIView.as_view(),name='users_api_user'),
]