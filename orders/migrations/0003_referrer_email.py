# Generated by Django 3.1.3 on 2020-11-28 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_referrer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='referrer',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]