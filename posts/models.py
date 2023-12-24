from django.db import models
from django.contrib.auth.models import User
from places.models import Place


class Post(models.Model):
    # We will have the possibility of choosing between different filters
    # for the images
    image_filter_choices = [
    ('_1977', '1977'), ('brannan', 'Brannan'),
    ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
    ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
    ('kelvin', 'Kelvin'), ('normal', 'Normal'),
    ('nashville', 'Nashville'), ('rise', 'Rise'),
    ('toaster', 'Toaster'), ('valencia', 'Valencia'),
    ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    visit_date = models.DateField()
    content = models.TextField()
    image = models.ImageField(
        upload_to='positive/post_pictures/',
        default='../default_post_zlhcpb',
        blank=True
        )
    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices,
        default='normal'
        )
    recommendation = models.TextField(blank=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'