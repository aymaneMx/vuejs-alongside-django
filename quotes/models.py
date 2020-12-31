from django.db import models


class Quote(models.Model):
    value = models.TextField()
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=50)

    class Meta:
        ordering = ["-up_votes", ]

    def __str__(self):
        return (
            f"quote: {self.value}" 
            f"author: {self.author}" 
            f"upvotes: {self.up_votes}" 
            f"downvotes: {self.down_votes}"
        )
