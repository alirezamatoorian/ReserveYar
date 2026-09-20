import re
from rest_framework import serializers

def normalize_iranian_phone(value):
    value = value.strip().replace(' ', '').replace('-', '')
    if value.startswith('+98'):
        value = '0' + value[3:]
    elif value.startswith('0098'):
        value = '0' + value[4:]
    elif value.startswith('98') and len(value) == 12:
        value = '0' + value[2:]

    if not re.fullmatch(r'09\d{9}', value):
        raise serializers.ValidationError('شماره موبایل معتبر نیست')
    return value