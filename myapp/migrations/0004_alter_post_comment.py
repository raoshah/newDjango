# Generated by Django 3.2.20 on 2023-07-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.CharField(max_length=100),
        ),
    ]