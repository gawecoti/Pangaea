from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r"^$", views.FeedView.as_view(), name="feed"),
    url(r"topic/add/$", views.TopicAdd.as_view(), name="topic_add"),
    url(r"topic/(?P<pk>\d+)/$", views.TopicUpdate.as_view(), name="topic_update"),
    url(r"topic/(?P<pk>\d+)/delete/$", views.TopicDelete.as_view(), name="topic_delete"),
    url(r"^(?P<slug>[\w-]+)/$", views.PostDetailView.as_view(), name="detail"),
    url(r"^topic/summary/add/$", views.CreateSummaryView.as_view(), name="summary_add"),
    url(r"^topic/story/add/$", views.CreateStoryView.as_view(), name="story_add")
)