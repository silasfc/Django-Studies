from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


'''
#Command in the  shell to create Blog ' Post
# TO INSTALL: pip install fake-factory
import random
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from faker import Factory
fake = Factory.create()
s = ' '
user = User.objects.first()
from blog.models import  Post
for item in range(1,41):
    author = fake.name()
    title = s.join(fake.words(random.randint(4,16)))
    slug = slugify(title)
    #slugify the title
    status = 'published'
    body = s.join(fake.paragraphs(random.randint(2,10)))
    book = Post.objects.create(title=title, author=user, status=status, body=body, slug=slug )
    print(author)
    book.save()
'''


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )
