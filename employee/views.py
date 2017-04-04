#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import transaction
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from django.views import generic
from models import (
    Employee,
    TalkRecord,
    PositionRecord,
    LevelRecord,
    DegreeAndGrossRecord
)

class ListEmployee(LoginRequiredMixin, generic.TemplateView):
    """Generic view to list employee requests """
    template_name = 'employee/list.html'

    def get_context_data(self, **kwargs):
        """Retrieve context data<"""
        context = super(ListEmployee, self).get_context_data(**kwargs)

        context['object_list'] = Employee.objects.all()

        return context

class ViewEmployee(LoginRequiredMixin, generic.DetailView):
    template_name = 'employee/view.html'
    model = Employee

    def get_context_data(self, **kwargs):
        print self.kwargs.get(self.pk_url_kwarg, None)
        context = super(ViewEmployee,self).get_context_data(**kwargs)
        context["talk_list"] = TalkRecord.objects.filter(tr_related_emp = context["employee"]).order_by('-create_date')
        context["position_record_list"] = PositionRecord.objects.filter(pr_related_emp = context["employee"]).order_by('-create_date')
        context["level_record_list"] = LevelRecord.objects.filter(lr_related_emp = context["employee"]).order_by('-create_date')
        context["dg_record_list"] = DegreeAndGrossRecord.objects.filter(dgr_related_emp = context["employee"]).order_by('-create_date')
        print context
        return context


@csrf_exempt
def saveBasic(request):
    tag = request.POST.get("tag")
    data = request.POST.get("data")
    eid = request.POST.get("eid")
    e = Employee.objects.get(id = eid)

    if tag == "mobile":
        e.mobile = data
    elif tag == "address":
        e.address = data
    elif tag == "sex":
        if data == "男":
            e.sex = 1
        else:
            e.sex = 2
    elif tag == "birth":
        e.birth = data
    else:
        pass
    e.save()
    return HttpResponse('ok')

@csrf_exempt
def savePosition(request):
    data = request.POST.get("data")
    eid = request.POST.get("eid")
    e = Employee.objects.get(id = eid)
    e.position = data
    e.save()

    p = PositionRecord(pr_title=data,pr_related_emp=e)
    p.save()

    return HttpResponse('ok')

@csrf_exempt
def saveLevel(request):
    data = request.POST.get("data")
    eid = request.POST.get("eid")
    e = Employee.objects.get(id = eid)
    e.level = data
    e.save()

    p = LevelRecord(lr_title=data,lr_related_emp=e)
    p.save()

    return HttpResponse('ok')


@csrf_exempt
def saveTalk(request):
    talkman = request.POST.get("talkman")
    data = request.POST.get("data")
    eid = request.POST.get("eid")
    e = Employee.objects.get(id = eid)

    p = TalkRecord(tr_title=talkman,tr_content=data,tr_related_emp=e)
    p.save()

    return HttpResponse('ok')