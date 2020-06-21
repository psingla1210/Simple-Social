from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    #path('', views.HomePageView.as_view(), name='home'),
    path('', views.ListGroups.as_view(), name='groups_list'),
    path('new/', views.CreateGroupView.as_view(), name='create'),
    path('posts/in/<slug>', views.SingleGroup.as_view(), name='single'),
    # path('join/<slug>', views.JoinGroup.as_view(), name='join'),
    # path('leave/<slug>', views.LeaveGroup.as_view(), name='leave'),
]
