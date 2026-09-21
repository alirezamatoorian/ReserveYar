from django.core.cache import cache
import secrets
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class OtpService:
    @staticmethod
    def generate_and_send_otp(phone_number):
        otp_code=str(secrets.randbelow(900000)+100000)
        cache_key=f'otp for {phone_number}'
        cooldown_key=f'cooldown for {phone_number}'
        if cache.get(cooldown_key):
            raise ValidationError("لطفا کمی صبر کنید و دوباره تلاش کنید")
        cache.set(cache_key,otp_code,timeout=60)
        cache.set(cooldown_key,True,timeout=60)
        print(f"otp for {phone_number}: {otp_code}")
        return True

    @staticmethod
    def verify_otp(phone_number,otp_code):
        cache_key=f'otp for {phone_number}'
        stored_code=cache.get(cache_key)
        if stored_code is None:
            raise ValidationError("Otp code is expired or not requested")
        if not secrets.compare_digest(otp_code,stored_code):
            raise ValidationError("Otp code is not valid")
        cache.delete(cache_key)
        try:
          user=User.objects.get(phone=phone_number)
        except User.DoesNotExist:
           user=User.objects.create_user(phone=phone_number)
        refresh=RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
