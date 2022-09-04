from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, EmailVerificationSerializer
from User.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .service import Service
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from schedule_planner_be.settings import SECRET_KEY


class RegisterView(generics.GenericAPIView):
    """Регистрация пользователя"""
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')

        absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
        email_body = 'Hi,' + user.first_name + '\n You have been registered at Belhard Academy Schedule Planner. ' \
                                              'Please, follow the link to sign in \n' + absurl
        data = {'email_body': email_body,
                'to_email': [user.email],
                'email_subject': 'Verify your email'}

        Service.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    """Верификация email"""
    queryset = User.objects.all()
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithm="RS256", options={"verify_signature": False})
            user = User.objects.get(id=payload['user_id'])
            if not user.email_verify:
                user.email_verify = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation link Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView): # доработать
    """Логин"""
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
