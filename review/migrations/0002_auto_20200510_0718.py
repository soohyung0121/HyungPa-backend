# Generated by Django 3.0.5 on 2020-05-10 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_comment',
            new_name='first_comment',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review_image',
            new_name='first_image',
        ),
    ]
