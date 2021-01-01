from django.urls import path

from todo.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]