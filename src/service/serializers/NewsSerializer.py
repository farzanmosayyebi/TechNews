from rest_framework import serializers

from data import models

class NewsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    tags = serializers.StringRelatedField(many = True)

    class Meta:
        model = models.News
        fields = [
            "id",
            "title",
            "text",
            "source",
            "tags"
        ]