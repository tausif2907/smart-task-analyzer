from django.db import models
try:
    # JSONField available in Django 3.1+
    from django.db.models import JSONField
except Exception:
    from django.contrib.postgres.fields import JSONField
class Task(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True)
    estimated_hours = models.FloatField(default=1.0)
    importance = models.IntegerField(default=5)
    dependencies = JSONField(default=list)  # list of task IDs
    def __str__(self):
        return self.title
