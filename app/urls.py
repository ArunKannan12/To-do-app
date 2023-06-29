from . import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", register.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path('',TaskList.as_view(),name='tasklist'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='taskdetail'),
    path('create_task/',TaskCreate.as_view(),name='taskcreate'),
    path('edit-task/<int:pk>/',TaskUpdate.as_view(),name='taskedit'),
    path('delete-task/<int:pk>/',TaskDelete.as_view(),name='taskdelete'),
]
