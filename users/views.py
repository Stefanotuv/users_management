import urllib

import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMessage
# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from grouping.tokens import account_activation_token
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from allauth.account.views import LoginView, LogoutView, SignupView
from allauth.utils import get_form_class,get_request_param
from allauth.account.views import _ajax_response
from django.urls import reverse, reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from . import app_settings
from django.shortcuts import resolve_url
from allauth.account.adapter import get_adapter, DefaultAccountAdapter
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.files import File
import os
from pathlib import Path

from allauth.account.utils import (
    complete_signup,
    get_login_redirect_url,
    get_next_redirect_url,
    logout_on_password_change,
    passthrough_next_redirect_url,
    perform_login,
    sync_user_email_addresses,
    url_str_to_user_pk,
)

import glob
from django.conf import settings

def activate(request, uidb64, token):
    try:
        # https://stackoverflow.com/questions/70382084/import-error-force-text-from-django-utils-encoding
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            mail_subject = 'Activate your blog account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': user.email,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # 'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()

            username = form.cleaned_data.get('email')
            messages.success(request,f'Account created for {username}!')

            # return HttpResponse('Please confirm your email address to complete the registration')
            return redirect('users_signup_email_ok')

            # return redirect('users_login')
    else:
        form = UserRegisterForm()
    # return render(request, 'users/login.html', {'form': form})
    email = request.POST['email']
    messages.error(request, f'{email} already existing, try another email!')

    return redirect('users_signup_email_ko')

# old implementation with function
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST,instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request,f'Account update successfully!')
#             return redirect('users_profile')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form':u_form,
#         'p_form':p_form
#     }
#
#     return render(request, 'users/profile.html',context)

class UserLoginView(LoginView):
        form_class = UserLoginForm
        template_name = "users/login.html"

        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        def get_context_data(self, **kwargs):
            ret = super(LoginView, self).get_context_data(**kwargs)
            signup_url = passthrough_next_redirect_url(self.request,
                                                       reverse("users_signup"),
                                                       self.redirect_field_name)
            redirect_field_value = get_request_param(self.request,
                                                     self.redirect_field_name)
            site = get_current_site(self.request)

            ret.update({"signup_url": signup_url,
                        "site": site,
                        "redirect_field_name": self.redirect_field_name,
                        "redirect_field_value": redirect_field_value})
            return ret

@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
        template_name = "users/logout.html"

        def get(self, *args, **kwargs):
            if app_settings.LOGOUT_ON_GET:
                return self.post(*args, **kwargs)
            if not self.request.user.is_authenticated:
                response = redirect(self.get_redirect_url())
                return _ajax_response(self.request, response)
            if self.request.user.is_authenticated:
                self.logout()
            ctx = self.get_context_data()
            response = self.render_to_response(ctx)
            return _ajax_response(self.request, response)

        def post(self, *args, **kwargs):
            url = self.get_redirect_url()
            if self.request.user.is_authenticated:
                self.logout()
            response = redirect(url)
            return _ajax_response(self.request, response)

        def get_redirect_url(self):
            return (
                    get_next_redirect_url(
                        self.request,
                        self.redirect_field_name) or get_adapter(
                self.request).get_logout_redirect_url(
                self.request))

class UserSignupOkView(SignupView):
    form_class = UserRegisterForm
    template_name = "users/emailconfirmationsent.html"
    # success_url = reverse_lazy('users_login')

# adding profile and register classes this would enable the
# change in template when called from other apps in the project

# class UserSignupView(SignupView):
#     form_class = UserRegisterForm
#     template_name = "users/signup.html"
#     # success_url = 'users/login.html'
#
#     def get(self, *args, **kwargs):
#         output = super().get(*args, **kwargs)
#         return output
#
#     def get_context_data(self, **kwargs):
#         ret = super(SignupView, self).get_context_data(**kwargs)
#         form = ret['form']
#         email = self.request.session.get('account_verified_email')
#         if email:
#             email_keys = ['email']
#             if app_settings.SIGNUP_EMAIL_ENTER_TWICE:
#                 email_keys.append('email2')
#             for email_key in email_keys:
#                 form.fields[email_key].initial = email
#         login_url = passthrough_next_redirect_url(self.request,
#                                                   reverse("users_login"),
#                                                   self.redirect_field_name)
#         redirect_field_name = self.redirect_field_name
#         redirect_field_value = get_request_param(self.request,
#                                                  redirect_field_name)
#         ret.update({"login_url": login_url,
#                     "redirect_field_name": redirect_field_name,
#                     "redirect_field_value": redirect_field_value})
#         return ret
#
#
#     def post(self, request, *args, **kwargs):
#         output = super().post(request,*args, **kwargs)
#         return output
@method_decorator(login_required, name='dispatch')
class UserProfileView(UpdateView):
    template_name = 'users/profile.html'
    # form_class = ProfileUpdateForm

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'users/profile.html', context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account update successfully!')
        return HttpResponseRedirect(reverse('users_profile', kwargs={'pk': kwargs['pk']}))


@method_decorator(login_required, name='dispatch')
class UserProfileChangePictureView(UpdateView):
    template_name = 'users/profile_change_picture.html'
    # form_class = ProfileUpdateForm
    context_object_name = 'profilechangeview'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get(self, request, *args, **kwargs):
        # u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)
        #
        # context = {
        #     'u_form': u_form,
        #     'p_form': p_form
        # }
        # os.getcwd() # get the current work directory

        # mylist = ['/'+f for f in glob.glob("users/media/profile_pics/gallery/*.*")]

        # current_dir = os. getcwd()
        # print('current_dir:')
        # print(current_dir)
        # print(settings.BASE_DIR)
        rdir = "users/media/profile_pics/gallery"
        # rdir = os.path.join(settings.MEDIA_ROOT,"profile_pics/gallery")
        mylist = ['/'+f for f in [os.path.join(rdir, fil) for fil in os.listdir(rdir)]]
        # # context = self.get_context_data(**kwargs)
        context = {'mylist': mylist}

        # print('glob.glob:')
        # print(glob.glob("users/media/profile_pics/gallery/*.*"))
        # print('mylist:')
        # print(mylist)
        return render(request, 'users/profile_change_picture.html', context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if len(request.FILES)!=0:
        # u_form = UserUpdateForm(request.POST, instance=request.user)
            user.profile.image = request.FILES['file']
            user.profile.save()
            # p_form = ProfileUpdateForm(request.POST,
            #                            request.FILES,
            #                            instance=request.user.profile)
            #
            # if p_form.is_valid():
            #     p_form.save()
            #     messages.success(request, f'Account update successfully!')
        else:

            pre_path = os.getcwd()
            path_suf = request.POST['selected'].split('/users')[1]
            new_path = Path(pre_path + '/users' + path_suf)
            image_url = new_path
            initial_path = user.profile.image.name

            # https: // stackoverflow.com / questions / 1308386 / programmatically - saving - image - to - django - imagefield
            # result = urllib.urlretrieve(image_url)

            user.profile.image.save(
                os.path.basename(new_path),
                File(open(image_url, 'rb'))
            )

            user.profile.save()



            # with new_path.open(mode='r') as f:
            #     ...
            #     new_image = File(f, name=new_path.name)
            # user.profile.image = new_image
            # user.profile.image = Image.open(new_path)
            # https: // docs.djangoproject.com / en / 4.0 / topics / files /
            # https: // stackoverflow.com / questions / 67702770 / unidentifiedimageerror - at - login - cannot - identify - image - file - c - users - sudha
            # user.save()
            # user.profile.save()
            # os.rename(initial_path, new_path)new_path
            # user.profile.image  = models.ImageField(default=full_path)




            # return redirect('users_profile')

        return HttpResponseRedirect(reverse('users_profile', kwargs={'pk': kwargs['pk']}))

@method_decorator(login_required, name='dispatch')
class UserChangePasswordView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('users_login')

    def get(self, request, *args, **kwargs):
        request.session['get_post'] = 'get'
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.session['get_post'] == 'post':
            if context['form'].is_valid():
                context['password_change'] = 'success'
            else:
                context['password_change'] = 'try again, there were some errors'

        elif self.request.session['get_post'] == 'get':
            context['password_change'] = ''
        return context
    def post(self, request, *args, **kwargs):
        request.session['get_post'] = 'post'
        return super().post(request, *args, **kwargs)