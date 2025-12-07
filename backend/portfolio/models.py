from django.db import models

# Create your models here.
class AboutPage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    additional_name = models.CharField(max_length=50, blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    headline = models.CharField(max_length=100, blank=True)
    about_me = models.TextField()
    markdown_body = models.TextField()
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return "About Page"

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"
    