from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin, )

    @action(detail=True, methods=['get', 'patch'],
            permission_classes=[
                'rest_framework.permissions.IsAuthenticated', ])
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
