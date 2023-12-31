# Generated by Django 4.2.4 on 2023-08-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_author_options_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name_plural': 'Books'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
        migrations.AddField(
            model_name='book',
            name='author_id',
            field=models.ManyToManyField(to='book.author'),
        ),
    ]
