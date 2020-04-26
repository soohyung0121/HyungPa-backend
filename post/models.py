from django.db import models
from user.models import User
from product.models import Product


class Post(models.Model):
    description  = models.CharField(max_length = 2000)
    like_number  = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)
    view_number  = models.IntegerField()
    user         = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    product      = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)

    class Meta:
        db_table = 'posts'

class PostComment(models.Model):
    comment            = models.CharField(max_length = 200)
    created_at         = models.DateTimeField(auto_now_add = True)
    user               = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    review             = models.ForeignKey('Post', on_delete = models.SET_NULL, null = True)
    post_comment_reply = models.ManyToManyField('self', symmetrical = False, through = 'PostCommentReply')

    class Meta:
        db_table = 'postcomments'

class PostCommentReply(models.Model):
    comment              = models.CharField(max_length = 200)
    created_at           = models.DateTimeField(auto_now_add = True)
    user                 = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    reply                = models.ForeignKey('PostComment', related_name = 'reply', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'postcommentreplies'
