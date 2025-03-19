from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)  # Campo para la biografía
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Campo para el avatar

    def __str__(self):
        return f'Profile of {self.user.username}'
