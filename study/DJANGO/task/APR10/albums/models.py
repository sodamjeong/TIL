from django.db import models
import os
from django.conf import settings

# Create your models here.

class Album(models.Model):
    content = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to="%Y/%m/%d/")

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Album, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_post = Album.objects.get(id=self.id)
            if self.image != old_post.image :
                if old_post.image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_post.image.path))
        super(Album, self).save(*args, **kwargs)