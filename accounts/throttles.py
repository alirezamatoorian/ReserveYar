from rest_framework.throttling import SimpleRateThrottle
from rest_framework.throttling import UserRateThrottle
from .validators import normalize_iranian_phone


class SendOtpPerPhoneThrottle(SimpleRateThrottle):
    scope = 'send_otp'

    def get_cache_key(self, request, view):
        phone=request.data.get('phone')
        if not phone:
            return None
        try:
            phone=normalize_iranian_phone(phone)
        except Exception:
            return None
        return f"otp-throttles:{phone}"