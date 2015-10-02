from django.conf.urls import url

<<<<<<< HEAD
#this url is used to tream bookmarks from a certain user
urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcadorapp.views.bookmark_user',
        name='marcadorapp_bookmark_user'),
    url(r'^$', 'marcadorapp.views.bookmark_list', name='marcadorapp_bookmark_list'),
=======
#this is a variable that puts url's in a string.
urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),#this initializes an empty string where one can view other peoples urls
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
]
>>>>>>> 00fa1f0da11a9f1ba3aa6cfb87eebc966b592675
