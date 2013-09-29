from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from model_utils.managers import QueryManager
from model_utils.models import TimeStampedModel
from PIL import Image

# Models
class Topic(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    creator = models.ForeignKey(User, related_name=u'topics')
    pic = models.ImageField(upload_to='img/', default='img/no-img.jpg')
    objects = models.Manager()

    # Set ouput format to unicode
    def __unicode__(self):
        return u'{0}'.format(self.name)

    # Save slug method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("topics:detail", (), {"slug": self.slug})

class Story(TimeStampedModel):
    story_title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, related_name=u'stories')

    def __unicode__(self):
        return u'{0}'.format(self.text)

class Summary(TimeStampedModel):
    text = models.TextField()
    topic = models.ForeignKey(Topic, related_name=u'summaries')

    def __unicode__(self):
        return u'{0}'.format(self.text)