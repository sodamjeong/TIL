from django.db import models
import os
from django.conf import settings
# from django.core.files.storage import default_storage

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    img_file = models.ImageField(null=True, upload_to="", blank=True)
    category_Choices = (('신기술', '신기술'), ('개발', '개발'), ('CS', 'CS'))
    category = models.CharField(max_length=20, choices=category_Choices)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def count_likes_user(self):
        return self.like_users.count()

    def delete(self, *args, **kargs):
        if self.img_file:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.img_file.path))
        super(Post, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_post = Post.objects.get(id=self.id)
            if self.img_file != old_post.img_file:
                if old_post.img_file:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_post.img_file.path))
        super(Post, self).save(*args, **kwargs)