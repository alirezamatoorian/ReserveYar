from rest_framework.throttling import SimpleRateThrottle
from rest_framework.throttling import UserRateThrottle


class SendOtpPerPhoneThrottle(SimpleRateThrottle):
    scope = 'send_otp'

    def get_cache_key(self, request, view):
        phone=request.data.get('phone')
        if not phone:
            return None
        raise f"otp for {phone}"