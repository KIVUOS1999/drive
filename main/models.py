from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    document = models.FileField()
    upload = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username


