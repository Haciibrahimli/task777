# Generated by Django 4.2.7 on 2023-11-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'ordering': ('name',), 'verbose_name': 'movzu', 'verbose_name_plural': 'movzular'},
        ),
    ]
