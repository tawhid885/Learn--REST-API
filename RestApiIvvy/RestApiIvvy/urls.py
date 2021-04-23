from django.contrib import admin
from django.urls import path
from api.views import taskView,apiOverview,taskDetail,taskCreate,taskDelete,taskUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',apiOverview,name='api'),
    path('task-view/',taskView,name='task-view'),
    path('task-create/',taskCreate,name='task-create'),
    path('task-detail/<str:pk>/',taskDetail,name='task-detail'),
    path('task-delete/<str:pk>/',taskDelete,name='task-delete'),
    path('task-update/<str:pk>/',taskUpdate,name='task-update'),
]
