from django.urls import path

from todo.views import home_view, TaskUpdateView, ListTasksView, TaskDeleteView

urlpatterns = [
    path('', home_view, name='home'),
    path('api/<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('api/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete-task'),
    path('api/', ListTasksView.as_view(), name='list-task'),
]