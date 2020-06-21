from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='groups_list'),
]
