from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from reviews.models import (Categories,
                            Genres,
                            Titles,
                            Reviews,
                            Comments)


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

    def validation_rating(self, value):
        if 0 >= value >= 10:
            raise serializers.ValidationError('Недопустимая оценка')
        return value


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
    )

    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('id', 'author', 'review')


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = '__all__'


class TitleGenreSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Categories.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genres.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        model = Genres
        fields = '__all__'


class TitlesSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(read_only=True)
    genre = GenresSerializer(read_only=True, many=True)
    rating = ...

    class Meta:
        model = Titles
        fields = '__all__'
