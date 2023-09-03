from django.contrib import admin
from .models import Post, Question, Youtube, Chat

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Youtube)
admin.site.register(Chat)