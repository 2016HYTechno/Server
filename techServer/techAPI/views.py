import random

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from techAPI.models import UserProfile


class UserList(APIView):

    def make_auth_key(self):
        auth_key = ''
        Strings = ['a','b','c','d','e','g','h','i','j','k','l','m',
                   'n','o','p','q','r','s','t','u','v','w','x','y','z',
                   '0','1','2','3','4','5','6','7','8','9']
        for i in range(0,15):
            auth_key = auth_key + Strings[random.randrange(0,35)]
        return auth_key

    def get(self,request,format= None):
        users = UserProfile.objects.all()

        if users.count() == 0:
            return Response('No users')
        