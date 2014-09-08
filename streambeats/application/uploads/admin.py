from django.contrib import admin
from models import Image, File


class ImageAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', )


class FileAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', )

admin.site.register(File, FileAdmin)
admin.site.register(Image, ImageAdmin)
