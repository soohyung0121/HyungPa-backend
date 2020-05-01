# Generated by Django 3.0.5 on 2020-04-28 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewcomment',
            name='comment_reply',
        ),
        migrations.AddField(
            model_name='reviewcomment',
            name='original_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='review.ReviewComment'),
        ),
        migrations.AlterModelTable(
            name='reviewcomment',
            table='review_comments',
        ),
        migrations.DeleteModel(
            name='CommentReply',
        ),
    ]
