from django.db import models
from django.conf import settings
import os

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)

    def delete(self, *args, **kargs):
        if self.imgfile:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.imgfile.path))
        super(Todo, self).delete(*args, **kargs)