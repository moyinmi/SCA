from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length= 100)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    pics = models.ImageField(default='img.jpg', upload_to = 'image', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)


    class Meta:
        verbose_name_plural = "articles"

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        super().save()