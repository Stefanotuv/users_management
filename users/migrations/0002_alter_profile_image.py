# Generated by Django 4.0 on 2022-01-02 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='./profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
