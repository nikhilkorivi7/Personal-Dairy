# Generated by Django 5.0 on 2023-12-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dairy_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
