from django.conf.urls import url

#this is a variable that puts url's in a string.
urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),#this initializes an empty string where one can view other peoples urls
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
]
