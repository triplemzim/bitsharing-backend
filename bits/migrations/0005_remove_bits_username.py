# Generated by Django 4.2.9 on 2024-01-12 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bits', '0004_bits_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bits',
            name='username',
        ),
    ]
