from django.contrib import admin
from .models import Post, Question, Youtube, Chat, library

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Youtube)
admin.site.register(Chat)
admin.site.register(library)