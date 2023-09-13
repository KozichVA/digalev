from django.urls import path
from .views import MainListView, ContactsView, ProductionView, ServiceView, ProjectCompletedView

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('main', MainListView.as_view(), name='main'),
    path('contact', ContactsView.as_view(), name='contacts'),
    path('service', ServiceView.as_view(), name='service'),
    path('production', ProductionView.as_view(), name='production'),
    path('project_completed', ProjectCompletedView.as_view(), name='project_completed')
    # path('404.html', )
]