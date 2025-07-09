from django.db import models
from django.contrib.auth.mixins import User
# Create your models here.
class Confessions(models.Model):
    confession = models.CharField(max_length=1001,help_text="Enter your shhhhh.....!!")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:30]
    
