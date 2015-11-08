# -*- coding: utf-8 -*-
from django.shortcuts import render

from haishin.models import * 
from haishin.serializers import *
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import parsers
from rest_framework import exceptions, HTTP_HEADER_ENCODING
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import *
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import *
from requests import request, HTTPError
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from django.core.mail import send_mail


# Normal authentication classes
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = (AllowAny,)
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = Token

    # Accepte un backend en parametre : 'auth' pour un login / pass classique
    def post(self, request, backend):
        #check if email is present, po5i patch:
        email_or_username = request.DATA.get("username")
        if email_or_username and '@' in email_or_username:
            user_request = get_object_or_404(
                    User,
                    email=email_or_username,
                )
            request.DATA["username"] = user_request.username
        
        #serialize the request
        serializer = self.serializer_class(data=request.DATA)

        if backend == 'auth':
            if serializer.is_valid():
                user = serializer.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'id': token.user.id})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            raise Http404
            """
            # saved for future use (social login)
            user = register_by_access_token(request, backend)
            
            if user and user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'id': user.id, 'userRole': 'user', 'token': token.key})
            else:
                return Response("User does not exists or email is already in use", status=status.HTTP_400_BAD_REQUEST)
            """



class ResetPassword(APIView):
    throttle_classes = ()
    permission_classes = (AllowAny,)
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = Token
    
    def post(self, request):
        email = request.data.get("email","")
        user = get_object_or_404(
                User,
                email=email,
        )
        
        random = get_random_string()
        user.set_password(random)
        user.save()
        
        send_mail('Cambio de contraseña para su cuenta',
                          u'Usted ha solicitado resetear su contraseña de cuenta. La puede cambiar cualquier momento editando su perfil.\n\nSu nueva contraseña temporal es:\n\n'+random,
                          'info@haishin.io',
                          [email], fail_silently=False)
        return Response({'status': 'ok'})

class ObtainLogout(APIView):
    throttle_classes = ()
    permission_classes = (IsAuthenticated,)
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = Token

    # Logout le user
    def get(self, request):
        #delete token
        if request.META.get('HTTP_AUTHORIZATION'):

            auth = request.META.get('HTTP_AUTHORIZATION').split()
            print auth

            if not auth or auth[0].lower() != b'token' or len(auth) != 2:
                msg = 'Invalid token header. No credentials provided.'
                return Response(msg, status=status.HTTP_401_UNAUTHORIZED)
            
            try:
                token = Token.objects.get(key=auth[1])
                if token and token.user.is_active:
                    token.delete()
                    #logout(request.user)
                    return Response({'status': 'ok'})
            except:
                return Response("Error, Tokes does not exists",status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response("Error, Not Authorized",status=status.HTTP_401_UNAUTHORIZED)










# --------------------------------------------------------------------------------
# API
# --------------------------------------------------------------------------------

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsAuthenticated()),

class DishViewSet(viewsets.ModelViewSet):
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        business_id = self.request.query_params.get('business_id', None)
        queryset = Dish.objects.filter(business_id=business_id,published=True) if business_id is not None else None
        return queryset

class BusinessViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        city_id = self.request.query_params.get('city_id', None)
        town_id = self.request.query_params.get('town_id', None)
        queryset = None
        if town_id is not None:
            queryset = Business.objects.filter(town__id=town_id)
        elif city_id is not None:
            queryset = Business.objects.filter(town__city__id=city_id)
        return queryset

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get_queryset(self):
        code = self.request.query_params.get('code', None)
        queryset = City.objects.filter(country__code=code) if code is not None else City.objects.all()
        return queryset
