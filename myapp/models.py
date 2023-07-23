from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=20)
    comment = models.CharField(max_length=60)

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