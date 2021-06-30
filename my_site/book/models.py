from django.db import models
from django.contrib.auth.models import User
class Genre(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    date_added=models.DateField(auto_now_add=True)
class Book(models.Model):
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE,default=False,db_constraint=False)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=300)
    description=models.TextField()
    published=models.DateField()
