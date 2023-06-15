from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers

from reviews.models import Reviews, Titles


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewsSerializer
    permission_classes = ()

    def get_queryset(self):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, pk=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentsSerializer
    permission_classes = ()

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
