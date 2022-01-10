from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer, UserSerializer

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.

class PatientView(viewsets.ModelViewSet):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

