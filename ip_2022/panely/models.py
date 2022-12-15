from django.db import models

# Create your models here.

class Panely_pvh(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=50)
    image = models.FileField('Фото', upload_to='panely/img/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Панель'
        verbose_name_plural = 'Панели'

class Ugolky(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=50)
    image = models.FileField('Фото', upload_to='panely/img/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Угол ПВХ'
        verbose_name_plural = 'Углы ПВХ'

class Complect_pvh(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=50)
    image = models.FileField('Фото', upload_to='panely/img/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Комплектующие для ПВХ'
        verbose_name_plural = 'Комплектующие для ПВХ'