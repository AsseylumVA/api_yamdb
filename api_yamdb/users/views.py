from random import randint

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import (UserSerializer, UserSingupSerializer,
                          UserCreateTokenSerializer)
from .permissions import IsAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin, )

    @action(detail=True, methods=['get', 'patch'],
            permission_classes=['IsAuthenticated'])
    def me_info(self, request):
        me = request.user

        if request.method == 'PATCH':
            serializer = self.get_serializer(me, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(me)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes(['AllowAny'])
def user_signup(request):
    data = request.data
    serializer = UserSingupSerializer(data=data)
    if serializer.is_valid:
        confirmation_code = randint(1000, 9999)
        email = serializer.data.get('email')
        send_mail(
            subject='confirmation code',
            message='Your confirmation code: {}'.format(confirmation_code),
            from_email='yamdb@defaultmail.com',
            recipient_list=[email],
        )
        serializer.save(confirmation_code=confirmation_code)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


@api_view(['POST'])
@permission_classes(['AllowAny'])
def user_create_token(request):
    data = request.data
    serializer = UserCreateTokenSerializer(data=request.data)
    if serializer.is_valid:
        user = get_object_or_404(User, username=data.get('username'))
        token = get_token_for_user(user)
        return Response({'token': token}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
