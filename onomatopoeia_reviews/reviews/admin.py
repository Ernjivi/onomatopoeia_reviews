from django.contrib import admin

from reviews.models import Movie, Review

class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0
    raw_id_fields = ['author']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
