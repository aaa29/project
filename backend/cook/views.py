from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import  Ing
from django.contrib.auth.models import User
from .serializers import IngSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import action, parser_classes, api_view, permission_classes, authentication_classes
from rest_framework.parsers import MultiPartParser, JSONParser, FileUploadParser
from django.core.files.base import ContentFile
import json

class IngViewSet(viewsets.ModelViewSet):
    queryset = Ing.objects.all()
    serializer_class = IngSerializer
    permission_classes = (AllowAny,)
    parser_classes = [MultiPartParser]