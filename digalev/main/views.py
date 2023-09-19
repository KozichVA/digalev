from django.shortcuts import render
from django.views.generic import ListView
from .models import CompletedWorks, Service, Category, Equipment, User, Order


class MainListView(ListView):
    template_name = 'main/index.html'
    model = Category
    queryset = model.objects.all()
    context_object_name = 'service_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['page_name'] = 'Главная страница'
        context['carousel_items'] = Service.objects.all().filter(is_published=True)
        context['equipments_list'] = Equipment.objects.all()
        context['category_list'] = Category.objects.all()
        context['completed_list'] = CompletedWorks.objects.all()
        context['service_list'] = Service.objects.all()
        return context

    def get_queryset(self):
        objs = CompletedWorks.objects.all()
        return objs


# CreateView
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
    context_object_name = 'equipments_list'

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
    context_object_name = 'service_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['page_name'] = 'Услуги'
        return context


class ProjectCompletedView(ListView):
    template_name = 'main/completed_works.html'
    model = CompletedWorks
    context_object_name = 'completed_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['page_name'] = 'Выполненные работы'
        return context

    def get_queryset(self):
        objs = CompletedWorks.objects.all()
        return objs
