
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/', views.TaskListview.as_view(), name = 'cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailview.as_view(), name= 'cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdatelview.as_view(), name= 'cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name= 'cbvdelete'),

]