# Generated by Django 4.2.2 on 2023-07-12 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='descritpion',
            new_name='description',
        ),
    ]
