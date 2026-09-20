from django.contrib.gis.gdal.prototypes.generation import void_output
from django.urls import path
from . import views



app_name = 'accounts'


urlpatterns = [
    path('send_otp/',views.SendOtpView.as_view(),name='sendOtp'),
    path('verify_otp/',views.VerifyOtpView.as_view(),name='verifyOtp'),
]