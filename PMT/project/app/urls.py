from django.urls import path,include
# from .views import *
from .import views
from .views import *
urlpatterns = [
    path('create/',views.create,name="create"),
    path('task/',views.task,name="task"),
    path('create_Project/',create_Project.as_view(),name="create_Project"),
    path('Create_Task/',Create_Task.as_view(),name="Create_Task"),
    path('Team_Member/',Team_Member.as_view(),name="Team_Member"),
]
