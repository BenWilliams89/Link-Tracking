# Generated by Django 4.2.17 on 2025-01-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
