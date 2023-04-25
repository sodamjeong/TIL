from django.db import models
from django.conf import settings
import os

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    def Article_image_path(instance, filename):
      return f'articles/{instance.title}/{filename}'
    image = models.ImageField(null=True, upload_to=Article_image_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Article, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_review = Article.objects.get(id=self.id)
            if self.image != old_review.image:
                if old_review.image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_review.image.path))
        super(Article, self).save(*args, **kwargs)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

