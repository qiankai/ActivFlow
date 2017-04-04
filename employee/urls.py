from django.conf.urls import url
from django.views.generic import TemplateView
from views import ListEmployee, ViewEmployee
from views import saveBasic,savePosition,saveTalk,saveLevel

urlpatterns = [
    url(
        r'^$', ListEmployee.as_view(),
        name='employee-list'
    ),
    url(
        r'^View/(?P<pk>\d+|None)/$',
        ViewEmployee.as_view(),
        name='employee-view'
    ),
    url(
        r'^api/savebasic$',
        saveBasic,
        name='employee-api-save'
    ),
    url(
        r'^api/saveposition$',
        savePosition,
        name='employee-api-position'
    ),
    url(
        r'^api/savetalk$',
        saveTalk,
        name='employee-api-talk'
    ),
    url(
        r'^api/savelevel$',
        saveLevel,
        name='employee-api-level'
    )
]