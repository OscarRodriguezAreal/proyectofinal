# Generated by Django 5.1.6 on 2025-03-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs_images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
