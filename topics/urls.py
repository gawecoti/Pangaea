from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r"^$", views.FeedView.as_view(), name="feed"),
    url(r"^(P<slug>[\w-]+)/$", views.PostDetailView.as_view(), name="detail"),
)