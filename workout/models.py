from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Workout(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text='Название тренировки')
    content = models.TextField(verbose_name=_('Содержание') ,help_text='Описание тренировки')
    type_workout = (
        ('po', 'Силовая'),
        ('fu', 'Функциональная'),
        ('ca', 'Кардио'),
        ('cr', 'Кросфит'),
        ('pi', 'Пилатес'),
        ('re', 'Реабилитационная'),
    )
    type = models.CharField(verbose_name=_('Тип') ,max_length=2, choices=type_workout, blank=True, default='po', help_text='Выбери вид тренировки')


    class Meta:
        ordering = ['type']

    def get_absolute_url(self):
        return reverse('workout-detail', args=[str(self.id)])


    def __str__(self):
        return self.title
