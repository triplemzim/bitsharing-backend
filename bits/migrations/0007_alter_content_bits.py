# Generated by Django 4.2.9 on 2024-01-12 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bits', '0006_alter_content_bits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='bits',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='bits.bits'),
            preserve_default=False,
        ),
    ]