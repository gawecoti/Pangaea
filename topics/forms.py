from django.forms import ModelForm
from .models import Topic, Summary, Story

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['name','pic']

class SummaryForm(ModelForm):
    class Meta:
        model = Summary
        fields = ['text']

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['story_title','url']
