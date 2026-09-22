from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import SendOtpSerializer, VerifyOtpSerializer, ProfileSerializer
from .services import OtpService
from .throttles import SendOtpPerPhoneThrottle,SendOtpPerIpThrottle,VerifyOtpPerPhoneThrottle

# Create your views here.



class SendOtpView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [SendOtpPerPhoneThrottle,SendOtpPerIpThrottle]
    def post(self,request):
        serializer=SendOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone=serializer.validated_data['phone']
        OtpService.generate_and_send_otp(phone)
        return Response({"message":"کد ورود با موفقیت ارسال شد"},status=status.HTTP_200_OK)

class VerifyOtpView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [VerifyOtpPerPhoneThrottle]
    def post(self,request):
        serializer_class = VerifyOtpSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        phone=serializer_class.validated_data['phone']
        code=serializer_class.validated_data['code']
        tokens=OtpService.verify_otp(phone,code)
        return Response({"message":"ورود موفقیت آمیز","tokens":tokens},status=status.HTTP_200_OK)

class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile

