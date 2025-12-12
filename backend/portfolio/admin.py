from django.contrib import admin
from .models import PortfolioProfile, AboutEntry, ExperienceEntry, ProjectEntry, SkillTag


@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "slug", "display_name", "headline", "updated_at")
    search_fields = ("user__username", "display_name", "headline", "slug")


@admin.register(AboutEntry)
class AboutEntryAdmin(admin.ModelAdmin):
    list_display = ("owner", "language", "headline", "updated_at")
    list_filter = ("language",)
    search_fields = ("owner__user__username", "headline", "about_me")


@admin.register(ExperienceEntry)
class ExperienceEntryAdmin(admin.ModelAdmin):
    list_display = ("owner", "position_title", "company_name", "start_date", "end_date", "is_current", "order")
    list_filter = ("is_current", "company_name")
    search_fields = ("position_title", "company_name", "owner__user__username")
    ordering = ("owner", "order", "-start_date")


@admin.register(ProjectEntry)
class ProjectEntryAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "slug", "highlight", "order")
    list_filter = ("highlight",)
    search_fields = ("title", "owner__user__username", "short_description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(SkillTag)
class SkillTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
