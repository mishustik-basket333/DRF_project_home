from django.db import models

from users.models import NULLABLE, User


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
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Course', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    PAY_METHOD = (
        ('cash', 'cash'),
        ('card', 'card'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    pay_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='оплаченный урок', **NULLABLE)
    sum = models.IntegerField(default=0, verbose_name='сумма оплаты')
    method = models.CharField(max_length=255, choices=PAY_METHOD, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user}, {self.pay_date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
