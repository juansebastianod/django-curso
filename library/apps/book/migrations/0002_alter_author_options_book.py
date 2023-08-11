# Generated by Django 4.2.4 on 2023-08-10 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'verbose_name_plural': 'Authors'},
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author')),
            ],
        ),
    ]