from django.db import models


class Task(models.Model):
    class Status(models.IntegerChoices):
        BACKLOG = 0, "backlog"
        TODO = 1, "todo"
        IN_PROGRESS = 2, "in progress"
        DONE = 3, "done"

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    status = models.PositiveIntegerField(choices=Status.choices, default=Status.BACKLOG)

    def __str__(self):
        return (
            f"task (" 
            f"title: {self.title}, " 
            f"status: {self.status})"
        )
