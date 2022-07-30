from django.db import models

# Create your models here.
class List(models.Model):
    title: "Characters" = models.CharField(max_length=150,null=False)
    duration: "Time" = models.CharField(max_length=50,null=True)

    def __str__(self):
        return "Title: " + self.title + " | " + "Duration: " + self.duration