from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=20)
    comment = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}: {self.comment}"
