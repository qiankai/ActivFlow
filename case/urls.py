from django.conf.urls import url
from django.views.generic import TemplateView
from views import ListCases, ViewCase, CreateCase

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
        CreateCase.as_view(),
        name='case-create'
    )
]