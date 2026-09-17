from django.core.cache import cache
import secrets




class OtpService:

    @staticmethod
    def generate_otp():
        otp_code=str(secrets.randbelow(900000)+100000)