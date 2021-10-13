from django.urls import path
from app1 import views

urlpatterns = [
    path('app1/', views.joke_list),
    path('app1/<int:pk>/', views.jokes_detail),
]
