# Generated by Django 3.1.3 on 2020-11-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(max_length=512),
        ),
    ]
