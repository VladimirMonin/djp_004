from django.db import models

# vacancies/models.py
import datetime

from django.db import models


class Vacancy(models.Model):
    STATUS = [  # Константа со списком вариантов поля статус. Это список картежей. Первое значение для базы, второе - человекочитаемое (пользователю АДМИНКИ)
        ('draft', 'Черновик'),
        ('open', 'Открыта'),
        ('closed', 'Закрыта'),
    ]

    slug = models.SlugField(max_length=100)  #
    text = models.CharField(max_length=2000)
    status = models.CharField(max_length=6, choices=STATUS, default='draft')  # Тут может быть 3 значения. Они называются енамами (т.е. перечислениями) указываются как константа сверху. Второй аргумент - выбор вариантов, третий, значение по умолчанию
    # created = models.DateField(default=datetime.date.now()) # Оно будет работать. Но есть более элегантный метод
    created = models.DateField(auto_now_add=True)  # Поставь текущее время на момент создания ;)

    def __str__(self):  # То что будет отображаться в заголовках админки
        return self.text