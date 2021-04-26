from rest_framework import serializers
from .models import  Ing
from django.contrib.auth.models import User


class IngSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ing
        fields = "__all__"