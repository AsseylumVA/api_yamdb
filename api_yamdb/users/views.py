from random import randint

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny
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
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)

    @action(detail=True, methods=['get', 'patch'],
            permission_classes=['IsAuthenticated', ])
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
@permission_classes([AllowAny])
def user_signup(request):
    data = request.data
    serializer = UserSingupSerializer(data=data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        username = serializer.validated_data.get('username')
        if (not User.objects.filter(username=username, email=email).exists()
            and (User.objects.filter(username=username).exists()
                 or User.objects.filter(email=email).exists())):
            return Response(
                'Username или Email уже занят!',
                status=status.HTTP_400_BAD_REQUEST
            )
        user, created = User.objects.get_or_create(
            username=username,
            email=email
        )
        confirmation_code = randint(1000, 9999)

        send_mail(
            subject='confirmation code',
            message='Your confirmation code: {}'.format(confirmation_code),
            from_email='yamdb@defaultmail.com',
            recipient_list=[email],
        )
        user.confirmation_code = confirmation_code
        user.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_create_token(request):
    serializer = UserCreateTokenSerializer(data=request.data)
    if serializer.is_valid():
        user = get_object_or_404(
            User,
            username=serializer.validated_data.get('username')
        )
        if (user.confirmation_code
                != serializer.validated_data.get('confirmation_code')):
            return Response(
                'Invalid confirmation_code',
                status=status.HTTP_400_BAD_REQUEST
            )

        token = get_token_for_user(user)
        return Response({'token': token}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
