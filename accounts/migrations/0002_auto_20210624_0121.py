# Generated by Django 3.1.12 on 2021-06-24 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myapplication',
            name='scopes',
            field=models.TextField(blank=True, null=True),
        ),
    ]