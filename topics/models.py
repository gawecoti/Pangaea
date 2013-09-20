from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from model_utils.managers import QueryManager
from model_utils.models import TimeStampedModel

# Models
class Topic(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    creator = models.ForeignKey(User, related_name=u'topics')
    objects = models.Manager()

    # Set ouput format to unicode
    def __unicode__(self):
        return u'{0}'.format(self.name)

    # Save slug method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)

class Story(TimeStampedModel):
    text = models.TextField()
    topic = models.ForeignKey(Topic, related_name=u'stories')

class Summaries(TimeStampedModel):
    text = models.TextField()
    topic = models.ForeignKey(Topic, related_name=u'summaries')