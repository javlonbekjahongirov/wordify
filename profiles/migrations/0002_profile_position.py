# Generated by Django 4.2.2 on 2023-06-21 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, max_length=221, null=True),
        ),
    ]
