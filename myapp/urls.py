from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('react/<int:id>', views.react, name='react'),
    path ('post/<int:post_id>', views.post, name='post'),
    path ('videos/', views.videos, name='videos')
]