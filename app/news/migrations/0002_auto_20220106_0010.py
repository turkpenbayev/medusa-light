# Generated by Django 3.1 on 2022-01-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
