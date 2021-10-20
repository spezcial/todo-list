from django.urls import path
from .views import TaskDetail, TaskList, TastCreate, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task-create/', TastCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
]