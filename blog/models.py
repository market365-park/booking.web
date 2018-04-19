from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from booking.models import User
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE', max_length=100)
    content = models.TextField('CONTENT', max_length=3000)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    owner = models.ForeignKey(User, null=True, auto_created=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table  = 'blog_posts'
        ordering  = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.id,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()