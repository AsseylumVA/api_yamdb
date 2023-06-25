from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import (CategoryViewSet,
                       CommentViewSet,
                       GenreViewSet,
                       ReviewViewSet,
                       TitleViewSet)

router = DefaultRouter()
router_titles = DefaultRouter()

router.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
router.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router_titles.register('', TitleViewSet, basename='titles')
router_titles.register(
    r'(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews',
)
router_titles.register(
    r'(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('', include(router.urls)),
    path('titles/', include(router_titles.urls)),
]
