from django.conf.urls import patterns, url

from article import views

urlpatterns = patterns('',
    url(r'^$',views.articles,name='articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$',views.article,name='article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$',views.addlike,name='addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$',views.addcomment,name='addcomment')
)