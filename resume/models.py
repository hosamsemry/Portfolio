from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200) 
    github = models.URLField(max_length=300)  
    description = models.TextField()  

    def __str__(self):
        return self.name
