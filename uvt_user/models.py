from django.db import models
from django.conf import settings

class UvtUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='uvt_user', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    ANR = models.CharField(max_length=255, blank=True)
    emplId = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name
