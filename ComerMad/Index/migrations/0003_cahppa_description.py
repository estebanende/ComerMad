# Generated by Django 4.2.8 on 2024-01-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0002_cahppa_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='cahppa',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
