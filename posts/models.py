from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to = 'picture/', blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    @property
    def likes_count(self):
        return self.post_likes.filter(is_active = True).count()

    def __str__(self):
        return f'Post {self.id} by {self.user.username}'

# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'post_likes')
    is_active = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('author', 'post')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name ='user_comments')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'post_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
