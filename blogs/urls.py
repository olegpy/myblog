from django.conf.urls import url
from blogs import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^new/$', views.add_post, name='add_post'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

]