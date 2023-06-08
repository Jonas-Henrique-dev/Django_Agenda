# Generated by Django 4.2.2 on 2023-06-08 22:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firt_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
