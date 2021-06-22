# Generated by Django 3.1.12 on 2021-06-17 08:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0002_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]