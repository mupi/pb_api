from django.conf.urls import patterns, include, url
from django.contrib import admin
#from core.views import AssociadoListView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pbapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^associado/$', AssociadoListView.as_view()),

)
