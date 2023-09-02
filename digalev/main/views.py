from django.shortcuts import render
from django.views.generic import ListView
from .models import CompletedWorks, Service, Category, Equipment, User, Order


class MainListView(ListView):
    template_name = 'index.html'
    model = Category


class ContactsView(ListView):
    template_name = 'contact.html'
    model = Category
