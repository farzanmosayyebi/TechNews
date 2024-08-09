from rest_framework import serializers

from data import models

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tag
        fields = [
            "title",
        ]