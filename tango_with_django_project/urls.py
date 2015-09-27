from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import
from registration.backends.simple.views import RegistrationView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portofolio.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='home'),
    url(r'^rango/', include('rango.urls')), # untuk menghubungkan urls.py yang ada di app
    url(r'^portofolio/', include('portofolio.urls')),
    url(r'^about$', views.about, name='about'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'


