from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, user_signup, user_create_token


router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/signup', user_signup, name='signup'),
    path('api/v1/auth/token', user_create_token, name='token'),
]
