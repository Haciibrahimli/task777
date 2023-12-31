# Generated by Django 4.2.7 on 2023-11-23 16:19

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='blog adi')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.upload_photo_to_blog)),
                ('subject', models.TextField(verbose_name='movzu')),
                ('reading_count', models.CharField(max_length=255, verbose_name='oxuma sayi')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
