# Generated by Django 5.1.4 on 2025-01-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='theme_color',
            field=models.CharField(default='blue', max_length=20),
        ),
    ]
