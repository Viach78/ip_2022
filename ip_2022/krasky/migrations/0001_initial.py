# Generated by Django 4.1.3 on 2022-12-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Krasky_vnut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('image', models.FileField(upload_to='krasky/img/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Краска врутри',
                'verbose_name_plural': 'Краски внутри',
            },
        ),
    ]
