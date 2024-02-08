from django.db import models

# Create your models here.
class dev_group(models.Model):
    CHOICES = [
        ("P", "Python"),
        ("H", "Html"),
        ("S", "Sql"),
        ("D", "Django"),
        ("Dl", "Data Science Libraries"),
        ("C", "CSS"),
        ("J", "Java Script"),
        ("G", "Git")
    ]
    name = models.CharField(max_length = 100)
    Tech_stack = models.CharField(max_length = 2, choices = CHOICES)
    email = models.EmailField(max_length = 50, null = False)
    Mobile_num = models.CharField(max_length = 12)