# Generated by Django 3.0.5 on 2020-04-28 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='product',
        ),
        migrations.RemoveField(
            model_name='postcomment',
            name='post_comment_reply',
        ),
        migrations.AddField(
            model_name='postcomment',
            name='original_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.PostComment'),
        ),
        migrations.AlterModelTable(
            name='postcomment',
            table='post_comments',
        ),
        migrations.DeleteModel(
            name='PostCommentReply',
        ),
    ]
