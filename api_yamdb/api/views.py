from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import IsAdminOrReadOnly, ReviewPermissions
from api.serializers import (CategoriesSerializer,
                             CommentsSerializer,
                             GenresSerializer,
                             ReviewsSerializer,
                             TitleGenreSerializer,
                             TitlesSerializer)
from reviews.models import (Categories,
                            Genres,
                            Titles,
                            Reviews)


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = (ReviewPermissions,)

    def get_queryset(self):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, pk=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)

    def get_queryset(self):
        review = get_object_or_404(
            Reviews,
            pk=self.kwargs.get('review_id'),
            title__id=self.kwargs.get('title_id'),
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Reviews,
            pk=self.kwargs.get('review_id'),
            title__id=self.kwargs.get('title_id'),
        )
        serializer.save(author=self.request.user, review=review)


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Categories.objects.all()


class GenresViewSet(viewsets.ModelViewSet):
    serializer_class = GenresSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Genres.objects.all()


class TitlesViewSet(viewsets.ModelViewSet):
    serializer_class = TitlesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Titles.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleGenreSerializer
        return TitlesSerializer
