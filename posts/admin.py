from django.contrib import admin
from posts.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date')

admin.site.register(Post, PostAdmin)