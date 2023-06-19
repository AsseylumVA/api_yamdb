from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoriesViewSet,
                       CommentsViewSet,
                       GenresViewSet,
                       ReviewsViewSet,
                       TitlesViewSet)

router_1 = DefaultRouter()
router_1.register(
    'categories',
    CategoriesViewSet,
    basename='categories'
)
router_1.register(
    'genres',
    GenresViewSet,
    basename='genres'
)
router_1.register(
    'titles',
    TitlesViewSet,
    basename='titles'
)
router_1.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='reviews'
)
router_1.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router_1.urls)),
]
