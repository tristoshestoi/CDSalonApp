from rest_framework import serializers

from Salon_app.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username")


class CdSerializer(serializers.ModelSerializer):

    class Meta:
        model = CD
        fields = ("price", "company_id")
