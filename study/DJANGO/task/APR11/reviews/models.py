from django.db import models
import os
from django.conf import settings
# from django.core.files.storage import default_storage

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    movie = models.CharField(max_length=100)
    title = models.CharField(max_length=80)
    img_file = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField(null=False)
    category = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def count_likes_user(self):
        return self.like_users.count()

    def delete(self, *args, **kargs):
        if self.img_file:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.img_file.path))
        super(Review, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_review = Review.objects.get(id=self.id)
            if self.img_file != old_review.img_file:
                if old_review.img_file:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_review.img_file.path))
        super(Review, self).save(*args, **kwargs)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)