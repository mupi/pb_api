from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import ProgramaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'programas', ProgramaViewSet, 'ProgramasList')
urlpatterns = router.urls

admin.autodiscover()


