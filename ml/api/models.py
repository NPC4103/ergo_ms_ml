from django.db import models

class MLModel(models.Model):
    name = models.CharField(
        max_length=255,
        default='Неизвестно',
        blank=True,
        unique=True
    )
    description = models.TextField(blank=True)
    model_id = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'ml'
        verbose_name = 'ML Model'
        verbose_name_plural = 'ML Models'

    def __str__(self):
        return self.name