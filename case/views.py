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

)


class ListCases(LoginRequiredMixin, generic.TemplateView):
    """Generic view to list employee requests """
    template_name = 'case/list.html'

    def get_context_data(self, **kwargs):
        """Retrieve context data<"""
        context = super(ListCases, self).get_context_data(**kwargs)

        context['object_list'] = CaseBaseInfo.objects.all()

        return context


class ViewCase(LoginRequiredMixin, generic.DetailView):
    template_name = 'case/view.html'
    model = CaseBaseInfo


class CreateCase(LoginRequiredMixin, generic.TemplateView):
    template_name = 'case/create.html'