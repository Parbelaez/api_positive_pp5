from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    place_type_choices = [
        ('restaurant', 'Restaurant'),
        ('bar', 'Bar'),
        ('cafe', 'Cafe'),
        ('hotel', 'Hotel'),
        ('museum', 'Museum'),
        ('park', 'Park'),
        ('beach', 'Beach'),
        ('other', 'Other')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    place_name = models.CharField(max_length=100)
    place_type = models.CharField(
        max_length=32,
        choices=place_type_choices,
        default='other'
        )
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='positive/place_pictures/',
        default='../default_place_zlhcpb',
        blank=True
        )
    
    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['place_name', 'city', 'address'],
                name='unique_place'
                )
        ]
    
    def __str__(self):
        return f'{self.place_name}'

