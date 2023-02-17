from django.conf import settings
from django.db import models
from django.utils.text import slugify


def get_unique_slug(slug):
    """
    Helper function to generate a unique slug for the post.
    """
    num = 1
    new_slug = slug
    while Post.objects.filter(slug=new_slug).exists():
        new_slug = '{}-{}'.format(slug, num)
        num += 1
    return new_slug


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    cover_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    github = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    overleaf = models.URLField(blank=True)
    archived = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.id:
            self.slug = get_unique_slug(self.slug)
        super(Post, self).save(*args, **kwargs)
