# Generated by Django 3.0.5 on 2020-05-06 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200504_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='skintone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.SkinTone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='skintype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.SkinType'),
        ),
    ]
