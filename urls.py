from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic import (CreateView, ListView, DetailView,
    RedirectView, TemplateView)
from wordviewer.models import WordEntry
from wordviewer.views import (register, WordEntryCreationView,
    WordEntryUpdateView, SitePreferencesUpdateView, AccountForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.contrib.auth.models import User

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url="/words/")),
    url(r'^create_entry/$', WordEntryCreationView.as_view(template_name="wordviewer/wordentry_form.html")),
    url(r'^update_entry/(?P<pk>\d+)/$', WordEntryUpdateView.as_view(template_name="wordviewer/wordentry_update.html")),
    url(r'^words/$', ListView.as_view(model=WordEntry, queryset=WordEntry.objects.order_by('name'))),
    url(r'^words/(?P<pk>\d+)/$', DetailView.as_view(model=WordEntry)), 
    url(r'^register/$', register),
    url(r'^login/$', login),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^sitepreferences/$', SitePreferencesUpdateView.as_view(success_url="/words/")),
    url(r'^administration/$', TemplateView.as_view(template_name='wordviewer/admin/administration.html')),
    url(r'^account/$', 'wordviewer.views.edit_account'),
    url(r'^studentstats/$', ListView.as_view(model=User, template_name='wordviewer/admin/user_list.html', queryset=User.objects.order_by('last_name', 'first_name'))),
    url(r'^students/(?P<pk>\d+)/$', DetailView.as_view(model=User, template_name='wordviewer/admin/user_detail.html',)), 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
