# Generated by Django 3.2.20 on 2023-07-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
