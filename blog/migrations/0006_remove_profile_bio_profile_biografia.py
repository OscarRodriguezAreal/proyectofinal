# Generated by Django 5.1.6 on 2025-04-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='biografia',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
