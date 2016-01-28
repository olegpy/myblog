from django.conf.urls import url
from blogs import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)/$',
        views.PostDetailView.as_view(), name='post_detail'),

    url(r'^new/$', views.PostCreateView.as_view(), name='add_post'),

    url(r'^edit/(?P<pk>\d+)/$',
        views.PostUpdateView.as_view(), name='edit_post'),

    url(r'^remove/(?P<pk>\d+)/$',
        views.PostDeleteView.as_view(), name='remove_post'),

    url(r'^add/(?P<pk>\d+)/comment/$',
        views.CommentCreateView.as_view(), name='add_comment_post'),

    url(r'^edit/(?P<pk>\d+)/comment/$',
        views.CommentUpdateView.as_view(), name='edit_comment'),

    url(r'^remove/(?P<pk>\d+)/comment/$',
        views.CommentDeleteView.as_view(), name='remove_comment'),

]
