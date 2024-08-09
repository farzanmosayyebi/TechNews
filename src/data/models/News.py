from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    source = models.URLField
    tags = models.ManyToManyField("Tag")

    def __str__(self) -> str:
        return self.title