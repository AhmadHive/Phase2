from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class project(models.Model):
    Team=models.ForeignKey(User,on_delete=models.CASCADE)
    project_url=models.URLField()
    Submitted_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Team.username

