from django.urls import path
from .views import TodoViewSet


urlpatterns = [
    path('todo/', TodoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('todo/<int:pk>/', TodoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]