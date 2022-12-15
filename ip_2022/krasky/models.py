from django.db import models

# Create your models here.

class Krasky_vnut(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=50)
    image = models.FileField('Фото', upload_to='krasky/img/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Краска врутри'
        verbose_name_plural = 'Краски внутри'

class Krasky_nar(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=50)
    image = models.FileField('Фото', upload_to='krasky/img/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Краска снаружи'
        verbose_name_plural = 'Краски снаружи'

class Krasky_aero(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=50)
    image = models.FileField('Фото', upload_to='krasky/img/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Краска в балончике'
        verbose_name_plural = 'Краски в балончиках'

class Krasky_rust(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=50)
    image = models.FileField('Фото', upload_to='krasky/img/')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Краска 3в1'
        verbose_name_plural = 'Краски 3в1'