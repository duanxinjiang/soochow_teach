# Generated by Django 4.2.3 on 2023-07-13 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]