# Generated by Django 4.2.2 on 2023-07-12 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tag_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('descritpion', models.TextField()),
                ('catblog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category_blog')),
            ],
        ),
    ]
