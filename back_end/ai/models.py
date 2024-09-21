from django.db import models

# Create your models here.


class Barrage(models.Model):
    rood_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    nature_of_words = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id},rood_id:{self.rood_id},name:{self.name},content:{self.content},nature_of_words:{self.nature_of_words}"
    
class Admin(models.Model):
    user_name = models.CharField(max_length=64)
    user_email = models.CharField(max_length=64)
    pass_word = models.CharField(max_length=64)

    def __str__(self):
        return f"user_name:{self.user_name},user_email:{self.user_email},pass_word:{self.pass_word}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Room(models.Model):
    rood_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.rood_id
