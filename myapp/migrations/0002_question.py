# Generated by Django 3.2.20 on 2023-07-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=120)),
                ('a', models.CharField(max_length=20)),
                ('b', models.CharField(max_length=20)),
                ('c', models.CharField(max_length=20)),
                ('d', models.CharField(max_length=20)),
                ('ans', models.CharField(max_length=20)),
            ],
        ),
    ]
