# Generated by Django 3.0.5 on 2020-04-28 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='followeruser',
            table='follower_users',
        ),
        migrations.AlterModelTable(
            name='skintone',
            table='skintones',
        ),
        migrations.AlterModelTable(
            name='skintype',
            table='skintypes',
        ),
        migrations.AlterModelTable(
            name='userskinproblem',
            table='user_skinproblems',
        ),
    ]
