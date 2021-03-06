# Generated by Django 2.2.11 on 2020-03-29 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0003_comment_comment_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('buy_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Buyer', to='bookshop.Book')),
            ],
            options={
                'db_table': 'Buyer',
                'verbose_name_plural': 'Покупатели',
                'verbose_name': 'Покупатель',
            },
        ),
    ]
