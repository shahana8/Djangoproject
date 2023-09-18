import uuid

from django.db import models
from users.models import Profile

class project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    description = models.TextField(null= True, blank= True)
    featured_image = models.ImageField(null= True, blank= True, default="default.jpg")
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    tags = models.ManyToManyField('tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title']


    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)

        return queryset


    @property
    def getVoteCount(self):
        review = self.review_set.all()
        upVote = review.filter(value='up').count()
        totalVote = review.count()

        ratio = (upVote / totalVote) * 100

        self.vote_total = totalVote
        self.vote_ratio = ratio
        self.save()

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'up vote'),
        ('down', 'down vote')
    )
    owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    body = models.TextField(null= True, blank= True)
    value = models.CharField(max_length=100, choices= VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    class Meta:
        unique_together = [['owner', 'project']]
    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def __str__(self):
        return self.name








