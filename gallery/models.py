from django.db import models
from filer.fields.image import FilerImageField


class SliderItem(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    image = FilerImageField(
        verbose_name='Изображение',
        on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Порядок'
    )

    class Meta:
        ordering = ('order',)
        verbose_name = 'Элемент слайдера'
        verbose_name_plural = 'Элементы слайдера'

    def __str__(self):
        return self.title
