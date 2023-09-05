from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}: {self.comment}"

class Question(models.Model):
    que = models.CharField(max_length=120)
    a = models.CharField(max_length=20)
    b = models.CharField(max_length=20)
    c = models.CharField(max_length=20)
    d = models.CharField(max_length=20)
    ans = models.CharField(max_length=20)

    # def __str__(self):
    #     return f"{self.que}: {self.a} , {self.b} , {self.c} , {self.d} , {self.ans}"

class Youtube(models.Model):
    title = models.CharField(max_length=40)  
    link = models.CharField(max_length=60)  

class Chat(models.Model):
    username = models.CharField(max_length=100)
    post = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

class library(models.Model):
    que = models.CharField(max_length=300)
    a = models.CharField(max_length=300)
    b = models.CharField(max_length=300)
    c = models.CharField(max_length=300)
    d = models.CharField(max_length=300)
    ans = models.CharField(max_length=300)

class Payment(models.Model):
    order_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')