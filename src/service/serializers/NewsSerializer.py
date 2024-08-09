from rest_framework import serializers

from data import models

class NewsSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many = True)
    class Meta:
        model = models.News
        fields = [
            "title",
            "text",
            "source",
            "tags"
        ]