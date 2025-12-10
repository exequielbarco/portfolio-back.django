from django.db import models
from django.conf import settings

class AboutPage(models.Model):
    LANGUAGE_TYPES = {"es": "Spanish", "en": "English"}

    additional_name = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_TYPES)
    image_url = models.URLField(max_length=500, blank=True)
    headline = models.CharField(max_length=100, blank=True)
    about_me = models.TextField(blank=True)
    markdown_body = models.TextField()
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="about_pages"
    )
    
    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
        
        constraints = [
            models.UniqueConstraint(
                fields=["user", "language"],
                name="unique_user_language"
            )
        ]


    def __str__(self):
        owner_name = self.owner.get_full_name() or self.owner.username
        return f"About Page {owner_name} - {self.get_language_display()}"


