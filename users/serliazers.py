from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
