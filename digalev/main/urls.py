from django.urls import path
from .views import MainListView, ContactsView


urlpatterns = [
    path('index.html', MainListView.as_view(), name='index'),
    path('contact.html', ContactsView.as_view(), name='contacts')
]