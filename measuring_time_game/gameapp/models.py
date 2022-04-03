from django.db import models
from django.conf import settings

# Create your models here.
class Record(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    verbose_name="投稿者",
                                    on_delete=models.CASCADE)
    record = models.FloatField("記録", blank=False)
    target_time = models.FloatField("目標時間", blank=False)
    created_at = models.DateTimeField("記録日", auto_now=True)

    def __str__(self):
        return f'{self.created_by} {str(self.created_at)}'
