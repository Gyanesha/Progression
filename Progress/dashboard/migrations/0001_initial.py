# Generated by Django 2.2.1 on 2019-05-24 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('about_myself', models.TextField()),
            ],
        ),
    ]
