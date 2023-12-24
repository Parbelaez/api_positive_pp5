from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Likes(models.Model):
    # We will have the possibility of choosing between different types
    # of likes: top, like, dislike.
    # The top like is when the user loves the place. Let's say, a can't miss.
    # The like is when the user likes the place.
    # The dislike is when the user doesn't like the place.
    like_type_choices = [
        ('top', 'Top'),
        ('like', 'Like'),
        ('dislike', 'Dislike')
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(
        Post,
        related_name='post_likes',
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    like_type = models.CharField(
        max_length=32,
        choices=like_type_choices,
        null=True
        )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} likes {self.post}'

