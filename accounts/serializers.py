from rest_framework import serializers
from .models import Profile
from .validators import normalize_iranian_phone




class SendOtpSerializer(serializers.Serializer):
    phone=serializers.CharField(max_length=11)

    def validate_phone(self,value):
        if not (value.isdigit() and len(value) == 11):
           raise serializers.ValidationError('Phone number must be digits')
        return normalize_iranian_phone(value)


class VerifyOtpSerializer(serializers.Serializer):
    phone=serializers.CharField(max_length=11)
    code=serializers.CharField(max_length=6)

    def validate_phone(self,value):
        if not (value.isdigit() and len(value) == 11):
           raise serializers.ValidationError('Phone number must be digits')
        return normalize_iranian_phone(value)

    def validate_code(self,value):
        if not (value.isdigit() and len(value) == 6):
            raise serializers.ValidationError('کد باید عدد و 6 رقمی باشد')
        return value


class ProfileSerializer(serializers.ModelSerializer):
    phone=serializers.CharField(source='user.phone',read_only=True)
    class Meta:
        model = Profile
        fields=["phone","first_name","last_name","email","no_show_count","suspended_until"]
        read_only_fields=["no_show_count","suspended_until"]