# Generated by Django 2.1.7 on 2019-02-22 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
    ]