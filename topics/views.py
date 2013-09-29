from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Topic, Story, Summary
from .forms import TopicForm, SummaryForm, StoryForm
from django.http import HttpResponseRedirect

# Feed view
class FeedView(ListView):
    model = Topic

    def get_template_names(self):
        return 'feed.html'

    def get_queryset(self):
        return self.model.objects.all()

# Topic views
class TopicAdd(CreateView):
    model = Topic
    form_class = TopicForm
    success_url = '/pangaea'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super(TopicAdd, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect('/')

class TopicUpdate(UpdateView):
    model = Topic
    fields = ['name']

class TopicDelete(DeleteView):
    model = Topic
    success_url = reverse_lazy('feed')

# Post view
class PostDetailView(DetailView):
    model = Topic
    context_object_name = 'topic'

    def get_template_names(self):
        return 'post.html'

    def get_context_data(self,**kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        topic = self.get_object()
        context['summary_list'] = Summary.objects.filter(topic=topic)
        context['story_list'] = Story.objects.filter(topic=topic)
        return context

class CreateSummaryView(CreateView):
    model = Summary
    fields = ['text']
    form_class = SummaryForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        title = form.data['title']
        self.object.topic = Topic.objects.get(name=title)
        self.object.save()
        return HttpResponseRedirect('/pangaea/' + form.data['slug'])

    def form_invalid(self, form):
        return HttpResponseRedirect('/pangaea' + form.data['slug'])

class CreateStoryView(CreateView):
    model = Story
    fields = ['title','url']
    form_class = StoryForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        title = form.data['title']
        self.object.topic = Topic.objects.get(name=title)
        self.object.save()
        return HttpResponseRedirect('/pangaea/' + form.data['slug'])

    def form_invalid(self, form):
        return HttpResponseRedirect('/pangaea/' + form.data['slug'])
