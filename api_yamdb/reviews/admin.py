from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from reviews.models import (Categories,
                            Genres,
                            Titles,
                            TitleGenre,
                            Reviews,
                            Comments)
from users.models import User


class UserResource(resources.ModelResource):

    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin):
    resource_classes = [UserResource]


admin.site.register(User, UserAdmin)


class CategoriesResource(resources.ModelResource):

    class Meta:
        model = Categories


class CategoriesAdmin(ImportExportModelAdmin):
    resource_classes = [CategoriesResource]


admin.site.register(Categories, CategoriesAdmin)


class GenresResource(resources.ModelResource):

    class Meta:
        model = Genres


class GenresAdmin(ImportExportModelAdmin):
    resource_classes = [GenresResource]


admin.site.register(Genres, GenresAdmin)


class TitlesResource(resources.ModelResource):

    class Meta:
        model = Titles


class TitlesAdmin(ImportExportModelAdmin):
    resource_classes = [TitlesResource]


admin.site.register(Titles, TitlesAdmin)


class TitleGenreResource(resources.ModelResource):

    class Meta:
        model = TitleGenre


class TitleGenreAdmin(ImportExportModelAdmin):
    resource_classes = [TitleGenreResource]


admin.site.register(TitleGenre, TitleGenreAdmin)


class ReviewsResource(resources.ModelResource):

    class Meta:
        model = Reviews


class ReviewsAdmin(ImportExportModelAdmin):
    resource_classes = [ReviewsResource]


admin.site.register(Reviews, ReviewsAdmin)


class CommentsResource(resources.ModelResource):

    class Meta:
        model = Comments


class CommentsAdmin(ImportExportModelAdmin):
    resource_classes = [CommentsResource]


admin.site.register(Comments, CommentsAdmin)
