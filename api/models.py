from django.db import models


class TemplateItem(models.Model):
    name = models.CharField(max_length=255, default='Без названия', blank=True, unique=True)
    description = models.TextField(blank=True)
    item_id = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'module_template'
        verbose_name = 'Template Item'
        verbose_name_plural = 'Template Items'

    def __str__(self):
        return self.name