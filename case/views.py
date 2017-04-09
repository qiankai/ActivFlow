# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.views import generic
from models import (
    CaseBaseInfo,
    Customer,
)
from employee.models import Employee


class ListCases(LoginRequiredMixin, generic.TemplateView):
    """Generic view to list employee requests """
    template_name = 'case/list.html'

    def get_context_data(self, **kwargs):
        """Retrieve context data<"""
        context = super(ListCases, self).get_context_data(**kwargs)

        context['object_list'] = CaseBaseInfo.objects.all()
        if self.request.user.has_perm('CAN_SE_CASE_CONFIRM'):
            context['confirmcase'] = True
        if self.request.user.has_perm('CAN_OPEN_CASE'):
            context['approvecase'] = True
        if self.request.user.has_perm('CAN_SALE_OPEN_CASE'):
            context['opencase'] = True
        return context


class ViewCase(LoginRequiredMixin, generic.TemplateView):
    template_name = 'case/view_0.html'

    def get_context_data(self, **kwargs):
        context = super(ViewCase, self).get_context_data(**kwargs)
        print self.kwargs
        print self.request.user.has_perm('CAN_SE_CASE_CONFIRM')
        pk = self.kwargs.get('pk')
        stage = self.kwargs.get('stage')
        '''
          stage:
                1: u'项目立项',
                2: u'项目投标',
                3: u'项目签约',
                4: u'项目实施',
                5: u'项目验收',
                6: u'维保阶段',
                0: u'关闭',
        '''
        try:
            e = CaseBaseInfo.objects.get(id = pk)
            if e.milestone == 1:
                context['casebaseinfo'] = e
                context['step'] = 1
                if self.request.user.has_perm('CAN_SE_CASE_CONFIRM'):
                    context['confirmcase'] = True
            elif e.milestone == 2:
                context['casebaseinfo'] = e
                context['step'] = 2
                if self.request.user.has_perm('CAN_OPEN_CASE'):
                    context['approvecase'] = True
            elif e.milestone == 3:
                context['casebaseinfo'] = e
                context['step'] = 3
            elif e.milestone == 99:
                context['casebaseinfo'] = e
                context['step'] = 99
        except CaseBaseInfo.DoesNotExist:
            context['customer_list'] = Customer.objects.all()
            context['presale_list'] = Employee.objects.filter(position__contains='售前')
            context['identifier'] = "B20170013"
            context['step'] = 0
        return context


class CreateCase(LoginRequiredMixin, generic.TemplateView):
    template_name = 'case/create.html'

    def get_context_data(self, **kwargs):
        """Retrieve context data<"""
        context = super(CreateCase, self).get_context_data(**kwargs)

        context['customer_list'] = Customer.objects.all()
        context['presale_list'] = Employee.objects.filter(position__contains='售前')
        context['identifier'] = "B20170013"

        return context



@csrf_exempt
def saveCustomer(request):
    data = request.POST.get("data")
    cid = request.POST.get("cid")
    c = Customer(identifier=cid,customer_title=data,create_user=request.user.username)
    c.save()
    return HttpResponse('ok')


@csrf_exempt
def openCase(request):
    case_title = request.POST.get("case_title")
    current_budget = request.POST.get("current_budget")
    case_deadline = request.POST.get("case_deadline")
    customer_title = request.POST.get("customer_title")
    contact_name = request.POST.get("contact_name")
    contact_mobile = request.POST.get("contact_mobile")
    salesId = request.POST.get("salesId")
    seId = request.POST.get("seId")
    identifer = request.POST.get("identifer")

    c = Customer.objects.get(id = customer_title)
    sales = Employee.objects.get(id = salesId)
    presales = Employee.objects.get(id = seId)

    p = CaseBaseInfo(
        identifier=identifer,
        case_title=case_title,
        case_deadline=case_deadline,
        contact_mobile=contact_mobile,
        contact_name=contact_name,
        customer_title=c,
        sales= sales,
        presales= presales,
        current_budget= current_budget,
        milestone = 1
    )

    p.save()
    return HttpResponse(str(p.id))

@csrf_exempt
def saveseconfirm(request):
    se_current_budgget = request.POST.get("se_current_budgget")
    se_case_deadline = request.POST.get("se_case_deadline")
    se_pro_descript = request.POST.get("se_pro_descript")
    cid = request.POST.get("cid")

    c = CaseBaseInfo.objects.get(id = cid)
    c.se_case_baseinfo = se_pro_descript
    c.se_case_deadline = se_case_deadline
    c.se_current_budget = se_current_budgget
    c.milestone = 2

    c.save()

    return HttpResponse(str(c.id))

@csrf_exempt
def approvecase(request):
    cid = request.POST.get("cid")
    c = CaseBaseInfo.objects.get(id=cid)
    c.milestone = 3
    c.save()
    return HttpResponse(str(c.id))

@csrf_exempt
def rejectcase(request):
    cid = request.POST.get("cid")
    c = CaseBaseInfo.objects.get(id=cid)
    c.milestone = 99
    c.save()
    return HttpResponse(str(c.id))