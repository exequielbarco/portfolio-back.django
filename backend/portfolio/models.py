from django.db import models
from django.conf import settings
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Language(TimeStampedModel):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.code})"


class SkillTag(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class PortfolioProfile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="portfolio",
    )

    slug = models.SlugField(max_length=50, unique=True)

    display_name = models.CharField(max_length=100, blank=True)
    headline = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar_url = models.URLField(max_length=500, blank=True)
    github_url = models.URLField(max_length=150, blank=True)
    linkedin_url = models.URLField(max_length=150, blank=True)

    languages = models.ManyToManyField(Language, related_name="portfolio", blank=True)

    def __str__(self):
        return f"Portfolio: {self.user.get_username()}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.user.get_username())
            slug = base_slug
            counter = 1
            while (
                PortfolioProfile.objects.filter(slug=slug).exclude(pk=self.pk).exists()
            ):
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class AboutEntry(TimeStampedModel):
    owner = models.ForeignKey(
        PortfolioProfile, on_delete=models.CASCADE, related_name="about"
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="about",
    )

    about_me = models.TextField(max_length=500, blank=True)

    markdown_body = models.TextField(blank=True)

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
        unique_together = ("owner", "language")

    def __str__(self):
        return f"AboutPage {self.owner.user.get_username()} ({self.language.code})"


class EducationEntry(TimeStampedModel):
    owner = models.ForeignKey(
        PortfolioProfile,
        on_delete=models.CASCADE,
        related_name="education",
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="education",
    )

    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    markdown_body = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-start_date"]
        verbose_name = "Education Page"
        verbose_name_plural = "Education Pages"

    def __str__(self):
        return f"{self.degree} @ {self.institution} ({self.owner.user.get_username()} - {self.language.code})"


class ExperienceEntry(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="experiences",
    )

    position_title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    description = models.TextField(blank=True)
    description_md = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-start_date"]
        verbose_name = "Experience Pages"
        verbose_name_plural = "Experience Pages"

    def __str__(self):
        return f"{self.position_title} @ {self.company_name} ({self.owner.user.get_username()})"


class ProjectEntry(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=80)
    short_description = models.CharField(max_length=255, blank=True)

    markdown_body = models.TextField()

    image_url = models.URLField(max_length=500, blank=True)
    repo_url = models.URLField(max_length=500, blank=True)
    live_url = models.URLField(max_length=500, blank=True)
    
    skills = models.ManyToManyField(SkillTag, blank=True, related_name="projects")


    highlight = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("owner", "slug")
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"{self.title} ({self.owner.user.get_username()})"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while (
                ProjectEntry.objects.filter(owner=self.owner, slug=slug)
                .exclude(pk=self.pk)
                .exists()
            ):
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
