from django.urls import path
from . import views



app_name = 'accounts'


urlpatterns = [
    path('send_otp/',views.SendOtpView.as_view(),name='sendOtp'),
    path('verify_otp/',views.VerifyOtpView.as_view(),name='verifyOtp'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
]