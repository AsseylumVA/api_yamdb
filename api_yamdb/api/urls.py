from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoriesViewSet,
                       CommentsViewSet,
                       GenresViewSet,
                       ReviewsViewSet,
                       TitlesViewSet,
                       UserViewSet)

router_1 = DefaultRouter()
router_1.register(
    'categories',
    CategoriesViewSet,
    base_name='categories'
)
router_1.register(
    'genres',
    GenresViewSet,
    base_name='genres'
)
router_1.register(
    'titles',
    TitlesViewSet,
    base_name='titles'
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
router_1.register(
    'users',
    UserViewSet
)

urlpatterns = [
    path('v1/', include(router_1.urls)),
]
