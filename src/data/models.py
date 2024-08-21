from django.db import models


class News(models.Model):
    title = models.CharField(max_length = 255, null = True)
    text = models.TextField()
    source = models.URLField(null = True, blank = True)
    tags = models.ManyToManyField("Tag")

    class Meta:
        verbose_name_plural = "News"

    def __str__(self) -> str:
        return self.title
    
    
class Tag(models.Model):
    title = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.title