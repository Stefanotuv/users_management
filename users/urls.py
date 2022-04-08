
from django.urls import path
from . import views
from .views import UserLoginView, UserLogoutView, UserChangePasswordView,UserSignupOkView, UserProfileView, UserProfileChangePictureView
from django.contrib.auth import views as auth_view

urlpatterns = [

    path("login/",UserLoginView.as_view(template_name='users/login.html'),name='users_login'),
    path("login/",UserLoginView.as_view(template_name='users/login.html'),name='account_login'),
    path('signup/', views.register, name='users_signup'),
    path('signup/email_confirmation_ok',UserSignupOkView.as_view(template_name='users/emailconfirmationsent_ok.html'), name='users_signup_email_ok'),
    path('signup/email_confirmation_ko', UserSignupOkView.as_view(template_name='users/emailconfirmationsent_ko.html'),
         name='users_signup_email_ko'),
    path('logout/',UserLogoutView.as_view(template_name='users/logout.html'),name='users_logout'),


    path('profile/', UserProfileView.as_view(template_name='users/profile.html'),name='users_profile'),

    # path('profile/change_picture', views.profile, name='users_profile'),
    # profile_change_picture.html
    # path('change_password/',auth_view.PasswordChangeView.as_view(),name='change_password'), # uses default template
    # path('change_password/', auth_view.PasswordChangeView.as_view(template_name='users/change_password.html'), name='change_password') # uses custom template

    path('profile/change_picture/', UserProfileChangePictureView.as_view(template_name='users/change_password.html'), name='user_change_picture'), # uses custom template

    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

    # path('profile/',views.profile,name='users_profile'), # old implementation with function

]