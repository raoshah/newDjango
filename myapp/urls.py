from django.urls import path
from myapp import views

urlpatterns = [
    path ('', views.home, name='home'),
    path ('react/<int:id>', views.react, name='react'),
    path ('libra/<int:id>', views.libra, name='libra'),
    path ('post/<int:post_id>', views.post, name='post'),
    path ('videos/', views.videos, name='videos'),
    path ('about/', views.about, name='about'),
    path ('contact/', views.contact, name='contact'),
    path ('chat/', views.chat, name='chat'),
    path ('register/', views.register, name='register'),
    path ('user_login/', views.user_login, name='user_login'),
    path ('user_logout/', views.user_logout, name='user_logout'),
    path ('profile/', views.profile, name='profile'),
    path ('create_order', views.create_order, name='create_order'),
    path ('payment/<str:order_id>,<int:amount>,<str:description>/', views.payment_view, name='payment_view'),
    path ('verify-payment/', views.verify_payment, name='verify_payment'),
    path ('upload/', views.photo_to_pdf, name='upload'),
    path ('get_suggestions/', views.get_suggestions, name='get_suggestions'),
    path ('libr/', views.libr, name='libr'),
    path ('rjgk/', views.rjgk, name='rjgk'),
]