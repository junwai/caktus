from django.urls import path
from . import views

app_name = 'art'

urlpatterns = [
    path('drill/', views.drill),
    #path('guess/', views.guess),
    path('answer/<int:pk>/', views.AnswerView.as_view(), name='answer')
]