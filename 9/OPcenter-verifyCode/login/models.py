from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20,unique=True,null=False)
    user_pw = models.CharField(max_length=128,unique=True,null=False)
    no_login = models.IntegerField(default=1,null=False)
    def __str__(self):
       return self.user_name,self.user_pw