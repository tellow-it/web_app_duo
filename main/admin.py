from django.contrib import admin

from main.models import FeedBack, Post


class PostAdmin(admin.ModelAdmin):
    Model = Post
    list_display = ['id', 'name', 'description', 'information']


admin.site.register(FeedBack)
admin.site.register(Post, PostAdmin)
