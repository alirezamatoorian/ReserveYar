from django.urls import path
from . import views



app_name = 'accounts'


urlpatterns = [
    path('otp/send/',views.SendOtpView.as_view(),name='sendOtp'),
    path('otp/verify/',views.VerifyOtpView.as_view(),name='verifyOtp'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
]