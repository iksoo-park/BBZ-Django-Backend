from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class AccountView(viewsets.ViewSet):
    def checkEmailDuplication(self, request):
        print("checkEmailDuplication()")