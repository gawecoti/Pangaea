from django.views.generic import ListView, DetailView
from .models import Topic

class FeedView(ListView):
    model = Topic

    def get_template_names(self):
        return 'feed_local.html'

class PostDetailView(DetailView):
    model = Topic

    def get_template_names(self):
        return 'post_local.html'
