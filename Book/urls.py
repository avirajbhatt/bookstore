from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, about, contact, signup, loginpage, logoutUser, addbook, showbook, thankyou

urlpatterns = [

    path('', index, name='home'),
    path('about', about),
    path('contact', contact),
    path('signup', signup, name='signup'),
    path('login', loginpage, name='login'),
    path('logout', logoutUser, name='logout'),
    path('addbook', addbook, name='addbook'),
    path('showbook', showbook, name='showbook'),
    path('thanks', thankyou, name='thankyou'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name ='password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]