import uuid

from django.db import models

class project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null= True, blank= True)
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    tags = models.ManyToManyField('tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'up vote'),
        ('down', 'down vote')
    )
    # owner =
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    body = models.TextField(null= True, blank= True)
    value = models.CharField(max_length=100, choices= VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def __str__(self):
        return self.name








