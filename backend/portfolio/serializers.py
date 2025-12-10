from django.contrib.auth.models import Group, User
from rest_framework import serializers
from backend.portfolio.models import AboutPage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name"]


class AboutPageSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="owner.first_name", read_only=True)
    last_name = serializers.CharField(source="owner.last_name", read_only=True)
    image_url = serializers.URLField()

    class Meta:
        model = AboutPage
        fields = [
            "id",
            "language",
            "first_name",
            "last_name",
            "additional_name",
            "image_url",
            "headline",
            "about_me",
            "markdown_body",
            "updated_at",
        ]
