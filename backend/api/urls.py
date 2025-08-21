from django.urls import path
from .views import UserList, UserDetail  # Adicione mais depois

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]