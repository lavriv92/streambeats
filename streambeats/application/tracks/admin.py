from django.contrib import admin

from .models import Artist, Album, Track, Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', )


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', )


class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
