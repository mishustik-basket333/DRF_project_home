from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    """Класс для отображения курсов"""
    name = models.CharField(max_length=100, verbose_name='название курса')
    pict = models.ImageField(upload_to='courses/', verbose_name='фото', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """Класс для отображения уроков"""
    name = models.CharField(max_length=100, verbose_name='название урока')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lessons/', verbose_name='фото', **NULLABLE)
    video_url = models.URLField(max_length=235, verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
