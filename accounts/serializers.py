from rest_framework import serializers
from .models import Profile




class SendOtpSerializer(serializers.Serializer):
    phone=serializers.CharField(max_length=11)

    def validate_phone(self,value):
        if not (value.isdigit() and len(value) == 11):
           raise serializers.ValidationError('Phone number must be digits')
        return value


class VerifyOtpSerializer(serializers.Serializer):
    phone=serializers.CharField(max_length=11)
    code=serializers.CharField(max_length=6)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields=["first_name","last_name","email","no_show_count","suspended_until"]
        read_only_fields=["no_show_count","suspended_until"]