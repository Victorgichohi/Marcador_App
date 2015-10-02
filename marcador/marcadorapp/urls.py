from django.conf.urls import url

#this url is used to tream bookmarks from a certain user
urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcadorapp.views.bookmark_user',
        name='marcadorapp_bookmark_user'),
    url(r'^$', 'marcadorapp.views.bookmark_list', name='marcadorapp_bookmark_list'),