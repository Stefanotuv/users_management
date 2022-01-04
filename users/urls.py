
from django.urls import path
from . import views
from .views import UserLoginView, UserLogoutView, UserChangePasswordView
from django.contrib.auth import views as auth_view

urlpatterns = [

    path("login/",UserLoginView.as_view(template_name='users/login.html'),name='users_login'),
    path('signup/', views.register, name='users_signup'),
    path('logout/',UserLogoutView.as_view(template_name='users/logout.html'),name='users_logout'),
    path('profile/',views.profile,name='users_profile'),
    # path('change_password/',auth_view.PasswordChangeView.as_view(),name='change_password'), # uses default template
    # path('change_password/', auth_view.PasswordChangeView.as_view(template_name='users/change_password.html'), name='change_password') # uses custom template
    path('change_password/', UserChangePasswordView.as_view(template_name='users/change_password.html'), name='user_change_password') # uses custom template
]