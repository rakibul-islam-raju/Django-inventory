# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.http import HttpResponse
# from django.urls import reverse
# from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, View
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.messages.views import SuccessMessageMixin

# from core.models import User


# class UserRole(View):
#     def get(self, *args, **kwargs):
#         users = User.objects.filter(is_active=True)
#         return HttpResponse(users)