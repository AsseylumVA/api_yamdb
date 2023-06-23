from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from reviews.models import (Category,
                            Genre,
                            Title,
                            TitleGenre,
                            Review,
                            Comment)
from users.models import User


class UserResource(resources.ModelResource):

    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin):
    resource_classes = [UserResource]


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = [CategoryResource]


class GenreResource(resources.ModelResource):

    class Meta:
        model = Genre


class GenreAdmin(ImportExportModelAdmin):
    resource_classes = [GenreResource]


class TitleResource(resources.ModelResource):

    class Meta:
        model = Title


class TitleAdmin(ImportExportModelAdmin):
    resource_classes = [TitleResource]


class TitleGenreResource(resources.ModelResource):
    title = Field(attribute='title_id', column_name="title_id")
    genre = Field(attribute='genre_id', column_name="genre_id")

    class Meta:
        model = TitleGenre


class TitleGenreAdmin(ImportExportModelAdmin):
    resource_classes = [TitleGenreResource]


class ReviewResource(resources.ModelResource):
    title = Field(attribute='title_id', column_name="title_id")

    class Meta:
        model = Review


class ReviewAdmin(ImportExportModelAdmin):
    resource_classes = [ReviewResource]


class CommentResource(resources.ModelResource):
    review = Field(attribute='review_id', column_name="review_id")

    class Meta:
        model = Comment


class CommentAdmin(ImportExportModelAdmin):
    resource_classes = [CommentResource]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(TitleGenre, TitleGenreAdmin)
admin.site.register(User, UserAdmin)
