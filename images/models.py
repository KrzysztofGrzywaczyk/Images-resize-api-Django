from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL

class Image(models.Model):
    user = models.ForeignKey(User, null=True, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='name')
    image = models.ImageField(upload_to='files', null=True)

    def __str__(self):
        return f"Image: {self.name}"
    
class Link(models.Model):
    user = models.ForeignKey(User, null=True, default=1, on_delete=models.CASCADE)
    img = models.IntegerField()
    expiration_time = models.IntegerField()

    def __str__(self):
        return f"{self.user}'s link"