from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#   Default model for every model is the objects manager. It retrieves all the objects in the database
#   Two ways to add or customize managers for models: add extra manager methods to an existing manager or create a new manager by modifying the initial QuerySet
#   First method provides a QuerySet like Post.objects.my_manager() notation and the latter provides you with a QuerySet notation like Post.my_manager.all()
class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )

class Post(models.Model):

    #   Enumeration class has subclassed models.TextChoices
    #   Django provides enumeration types that the dev can subclass to define choices simply
    #   They are based on the enum object of Python's standard library
    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        PUBLISHED = 'PB', 'Published'




    title = models.CharField(max_length=250)
    #   This is a SlugField field tha translates into a VARCHAR column
    #   Slug is a short label tha contains only letters, numbers, underscores, or hyphens
    #   SEO-friendly URLs for the blog posts
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    #Field to store the publication date and time
    publish = models.DateTimeField(default=timezone.now)
    #   used to store the date and time when the post is created
    created = models.DateTimeField(auto_now_add=True)
    #   store the last date and time when the post was created
    updated = models.DateField(auto_now=True)

    #   New field that is an instance of CharField
    status = models.CharField(
        max_length=2,
        #   The choices parameter limits the value of the field to the choices in Status
        choices=Status,
        #   default value is draft (enumeration value)
        default=Status.DRAFT,
    )

    #   model fields
    objects = models.Manager()
    published = PublishedManager()

    #   Many to One relationship with the default user model
    #   Each post is written by a user, and a user can write any number of posts
    #   Django will create a foreign key in the database using the primary key of the related model
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        #   specifies the behavior to adopt when the referenced object is deleted
        on_delete=models.CASCADE,
        #   specify the name of the reverse relationship, from user to posts
        related_name='blog_posts',
    )





    #   Defines metadata for the model.
    class Meta:
        #   use the ordering attribute to tell Django that it should sort results by the publish field
        ordering = ['-publish']
        #   allows dev to define database indexes for the model which can be one or multiple fields in ascending or descending order
        #   or functional expressions and database functions
        indexes = [
            models.Index(fields=['publish']),
        ]

 #   larger databases or those with a more complex structure may benefit from composite primary keys (joining table for a many-to-many relationship)
class FavoritePost(models.Model):
    pk = models.CompositePrimaryKey(
        "user", "post"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "blog.Post",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)

def __str__(self):
    #   Default python method to return a string
    #   Django will use this method to display the name of the object in many places
    return self.title