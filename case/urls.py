from django.conf.urls import url
from django.views.generic import TemplateView
from views import ListCases, ViewCase, CreateCase,saveCustomer,openCase

urlpatterns = [
    url(
        r'^$', ListCases.as_view(),
        name='case-list'
    ),
    url(
        r'^View/(?P<pk>\d+|None)/$',
        ViewCase.as_view(),
        name='case-view'
    ),
    url(
        r'^create/$',
        ViewCase.as_view(),
        name='case-create'
    ),
    url(
        r'^api/savecustomer',
        saveCustomer,
        name='case-api-savecustomer'
    ),
    url(
        r'^api/opencase',
        openCase,
        name='case-api-open'
    ),
]