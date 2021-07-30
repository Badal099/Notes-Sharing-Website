from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=40)
    subject = models.CharField(max_length=30)
    notesfile = models.FileField()
    filetype = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=1000,null=True)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username+" , "+self.status