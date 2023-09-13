from django.shortcuts import render
from django.views.generic import ListView
from .models import CompletedWorks, Service, Category, Equipment, User, Order


class MainListView(ListView):
    template_name = 'main/index.html'
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['page_name'] = 'Главная страница'
        return context


class ContactsView(ListView):
    template_name = 'main/contact.html'
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['page_name'] = 'Контакты'
        return context


class ProductionView(ListView):
    template_name = 'main/production.html'
    model = Equipment

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['page_name'] = 'Производство'
        return context

    def get_queryset(self):
        objs = Equipment.objects.all()
        return objs


class ServiceView(ListView):
    template_name = 'main/service.html'
    model = Service

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['page_name'] = 'Услуги'
        return context


class ProjectCompletedView(ListView):
    template_name = 'main/completed_works.html'
    model = CompletedWorks

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['page_name'] = 'Выполненные работы'
        return context

    def get_queryset(self):
        objs = CompletedWorks.objects.all()
        return objs
