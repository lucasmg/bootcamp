from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bootcamp.core.views.home', name='home'),
    url(r'^login/$', 'bootcamp.auth.views.login', name='login'),
    url(r'^logout/$', 'bootcamp.auth.views.logout', name='logout'),
    url(r'^signup/$', 'bootcamp.auth.views.signup', name='signup'),
    url(r'^feeds/$', 'bootcamp.feeds.views.feeds', name='feeds'),
    url(r'^feeds/post/$', 'bootcamp.feeds.views.post', name='post'),
    url(r'^feeds/like/$', 'bootcamp.feeds.views.like', name='like'),
    url(r'^feeds/comment/$', 'bootcamp.feeds.views.comment', name='comment'),
    url(r'^feeds/load/$', 'bootcamp.feeds.views.load', name='load'),
    url(r'^feeds/check/$', 'bootcamp.feeds.views.check', name='check'),
    url(r'^feeds/load_new/$', 'bootcamp.feeds.views.load_new', name='load_new'),
    url(r'^feeds/update/$', 'bootcamp.feeds.views.update', name='update'),
    url(r'^feeds/track_comments/$', 'bootcamp.feeds.views.track_comments', name='track_comments'),
    url(r'^questions/$', 'bootcamp.questions.views.questions', name='questions'),
    url(r'^questions/(\d+)/$', 'bootcamp.questions.views.question', name='question'),
    url(r'^questions/answered/$', 'bootcamp.questions.views.answered', name='answered'),
    url(r'^questions/unanswered/$', 'bootcamp.questions.views.unanswered', name='unanswered'),
    url(r'^questions/ask/$', 'bootcamp.questions.views.ask', name='ask'),
    url(r'^questions/favorite/$', 'bootcamp.questions.views.favorite', name='favorite'),
    url(r'^questions/answer/$', 'bootcamp.questions.views.answer', name='answer'),
    url(r'^questions/answer/accept/$', 'bootcamp.questions.views.accept', name='accept'),
    url(r'^questions/answer/vote/$', 'bootcamp.questions.views.vote', name='vote'),
    url(r'^articles/$', 'bootcamp.articles.views.articles', name='articles'),
    url(r'^articles/write/$', 'bootcamp.articles.views.write', name='write'),
    url(r'^articles/drafts/$', 'bootcamp.articles.views.drafts', name='drafts'),
    url(r'^articles/tag/(?P<tag_name>.+)/$', 'bootcamp.articles.views.tag', name='tag'),
    url(r'^articles/edit/(?P<id>\d+)/$', 'bootcamp.articles.views.edit', name='edit_article'),
    url(r'^admin/', include(admin.site.urls)),
)
