from django.conf.urls import url
from django.views.generic import TemplateView
from views import ListCases, ViewCase, CreateCase,saveCustomer,openCase,saveseconfirm,approvecase,rejectcase

urlpatterns = [
    url(
        r'^$', ListCases.as_view(),
        name='case-list'
    ),
    url(
        r'^View/(?P<pk>\d+|None)/Stage/(?P<stage>\d+|None)/$',
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
    url(
        r'^api/saveseconfirm',
        saveseconfirm,
        name='case-api-saveconfirm'
    ),
    url(
        r'^api/approvecase',
        approvecase,
        name='case-api-approvecase'
    ),
    url(
        r'^api/rejectcase',
        rejectcase,
        name='case-api-rejectcase'
    ),

]