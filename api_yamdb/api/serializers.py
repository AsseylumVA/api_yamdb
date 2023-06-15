from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from reviews.models import Comments, Reviews, Titles


class ReviewsSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Reviews
        fields = ('id', 'author', 'text', 'title', 'score', 'pub_date')

    def create(self, validated_data):
        request = self.context['request']
        author = request.user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Titles, pk=title_id)
        if Reviews.objects.filter(
                title=title,
                author=author).exists():
            raise serializers.ValidationError('Нельзя дважды оставить ревью')
        return Reviews.objects.create(**validated_data)


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
    )

    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('id', 'author', 'review')
