from django.conf.urls import url
from blogs import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^new/$', views.PostCreateView.as_view(), name='add_post'),
    # url(r'^new/$', views.add_post, name='add_post'),
    url(r'^edit/(?P<pk>\d+)/$',
        views.PostUpdateView.as_view(), name='edit_post'),
    # url(r'^(?P<pk>\d+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/$',
        views.PostDetailView.as_view(), name='post_detail'),
    # url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^remove/(?P<pk>\d+)/$',
        views.PostDeleteView.as_view(), name='remove_post'),

    url(r'^comment/(?P<pk>\d+)/$',
        views.CommentCreateView.as_view(), name='add_comment_post'),

    # url(r'^comment/(?P<pk>\d+)/$', views.add_comment_post, name='add_comment_post'),

]
