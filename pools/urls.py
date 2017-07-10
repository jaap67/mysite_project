from django.conf.urls import url
from pools import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^question/(?P<question_id>\d+)$', views.questions, name='question'),
	url(r'^question/(?P<question_id>\d+)/results$', views.results, name='results'),
	url(r'^question/(?P<question_id>\d+)/vote$', views.vote, name='vote'),
	url(r'^addvote/(?P<choice_id>\d+)$', views.addvote, name='addvote'),
	url(r'^question/(?P<question_id>\d+)/manage$', views.manage, name='manage'),
	url(r'^question/(?P<question_id>\d+)/remove/(?P<choice_id>\d+)$', views.withdrawChoice, name='remove'),
	url(r'^question/(?P<question_id>\d+)/change$', views.changeStatus, name='change'),
	url(r'^question/(?P<question_id>\d+)/add/(?P<choice_id>\d+)$', views.addchoice, name='addchoice'),
] 