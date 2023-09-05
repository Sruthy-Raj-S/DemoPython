from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('',views.index ,name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view(), name='cbupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(), name='cbvdelete')
]
