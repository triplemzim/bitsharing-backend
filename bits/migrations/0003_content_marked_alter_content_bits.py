# Generated by Django 4.2.9 on 2024-01-08 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bits', '0002_alter_bits_id_alter_content_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='bits',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='bits.bits'),
        ),
    ]
