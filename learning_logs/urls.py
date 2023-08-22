from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/<int:pk>', views.dashboard, name='dashboard'),
    path('topics', views.topics, name='topics'),
    path('topic/<int:pk>', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('new_entry/<int:pk>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:pk>', views.edit_entry, name='edit_entry'),
    path('delete_topic/<int:pk>', views.delete_topic, name='delete_topic'),
    path('delete_entry/<int:pk>', views.delete_entry, name='delete_entry'),
    path('paginator', views.paginator, name='paginator'),
    path('meeting', views.videocall, name='meeting'),
    path('new_meeting', views.new_meeting, name='new_meeting'),
    path('join_meeting', views.join_meeting, name='join_meeting')

]