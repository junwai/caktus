from django.urls import path
from . import views

app_name = 'art'

urlpatterns = [
    path('drill/', views.DrillView.as_view(), name='drill'),
    path('answer/', views.AnswerView.as_view(), name='answer')
]