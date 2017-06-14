from django.db import models

class ToDo(models.Model):
    title = models.CharField('título', max_length=200)
    order = models.PositiveIntegerField('ordem')
    done = models.BooleanField('feita', default=False)

    class Meta:
        ordering = ('order',)
