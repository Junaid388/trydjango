# Generated by Django 4.0.3 on 2022-03-28 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='contet',
            new_name='content',
        ),
    ]
