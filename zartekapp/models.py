from django.db import models

# Create your models here.
class Task(models.Model):
    post_name=models.CharField(max_length=200)
    post_desc=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/',default='images/none/noimg.jpg')
