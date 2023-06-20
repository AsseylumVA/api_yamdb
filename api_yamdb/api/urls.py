from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet,
                       CommentViewSet,
                       GenreViewSet,
                       ReviewViewSet,
                       TitleViewSet)

router_1 = DefaultRouter()
router_1.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
router_1.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router_1.register(
    'titles',
    TitleViewSet,
    basename='titles'
)
router_1.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_1.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router_1.urls)),
]
