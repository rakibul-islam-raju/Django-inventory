from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (View,
                                ListView,
                                CreateView,
                                UpdateView,
                                DeleteView,
                                TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Chalan_In, Chalan_Out
from .forms import ChalanInCreateForm, ChalanOutCreateForm


class ChalanInListCreateview(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        CreateView):
    model = Chalan_In
    template_name = 'chalan/chalan_in.html'
    form_class = ChalanInCreateForm
    success_url = 'chalan:chalan-in'
    success_message = "%(chalan_name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create New Chalan-In'
        context["chalan_in"] = Chalan_In.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class ChalanOutListCreateview(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        CreateView):
    model = Chalan_Out
    template_name = 'chalan/chalan_out.html'
    form_class = ChalanOutCreateForm
    success_url = 'chalan:chalan-out'
    success_message = "%(chalan_name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create New Chalan-Out'
        context["chalan_out"] = Chalan_Out.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)        

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

