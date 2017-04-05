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

        return context


class ViewCase(LoginRequiredMixin, generic.DetailView):
    template_name = 'case/view_0.html'
    model = CaseBaseInfo

    def get_context_data(self, **kwargs):
        context = super(ViewCase, self).get_context_data(**kwargs)
        print context


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
        current_budget= current_budget
    )

    p.save()
    return HttpResponse(str(p.id))