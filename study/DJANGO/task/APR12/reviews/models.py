from django.db import models
import os
from django.conf import settings
from django.utils import timezone
from datetime import timedelta,datetime
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
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


    @property
    def created_string(self):
        if self.created_at is None:
            return False

        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False
        
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    @property
    def created_string(self):
        if self.created_at is None:
            return False

        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False