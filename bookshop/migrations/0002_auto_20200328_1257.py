# Generated by Django 2.2.11 on 2020-03-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Имя'),
        ),
    ]
