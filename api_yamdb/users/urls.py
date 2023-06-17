from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, user_signup, user_create_token


router = DefaultRouter()
router.register('users', UserViewSet)

auth_v1 = [
    path('signup/', user_signup),
    path('token/', user_create_token),
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth_v1)),
]
