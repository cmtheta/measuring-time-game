from django.db import models
from django.conf import settings

# Create your models here.
class Record(models.Model):
    record = models.TextField("記録", blank=False)
    target_time = models.TextField("目標時間", blank=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    verbose_name="投稿者",
                                    on_delete=models.CASCADE)
    created_at = models.DateTimeField("記録日", auto_now=True)

    def __str__(self):
        return f'{self.created_by} {str(self.created_at)}'
