from django.conf.urls import patterns, include, url
from django.contrib import admin

from core import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^associado/$', views.AssociadoListView.as_view()),

	url(r'^programa/$', views.ProgramaListView.as_view()),
	url(r'^programa/(?P<pk>[0-9]+)/$', views.ProgramaDetailView.as_view()),

	url(r'^programa/list$', views.programa_list, name='programa_list'),
	url(r'^programa/new$', views.programa_create, name='programa_new'),
	url(r'^programa/edit/(?P<pk>\d+)$', views.programa_update, name='programa_edit'),
	url(r'^programa/delete/(?P<pk>\d+)$', views.programa_delete, name='programa_delete'),
)
