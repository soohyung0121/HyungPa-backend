# Generated by Django 3.0.5 on 2020-04-27 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200427_0643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='five',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='score',
            name='four',
        ),
        migrations.RemoveField(
            model_name='score',
            name='four_half',
        ),
        migrations.RemoveField(
            model_name='score',
            name='half',
        ),
        migrations.RemoveField(
            model_name='score',
            name='one',
        ),
        migrations.RemoveField(
            model_name='score',
            name='one_half',
        ),
        migrations.RemoveField(
            model_name='score',
            name='three',
        ),
        migrations.RemoveField(
            model_name='score',
            name='three_half',
        ),
        migrations.RemoveField(
            model_name='score',
            name='two',
        ),
        migrations.RemoveField(
            model_name='score',
            name='two_half',
        ),
        migrations.AlterModelTable(
            name='firstcategory',
            table='first_categories',
        ),
        migrations.AlterModelTable(
            name='secondcategory',
            table='second_categories',
        ),
        migrations.AlterModelTable(
            name='userscore',
            table='user_scores',
        ),
    ]
