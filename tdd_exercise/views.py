from django.shortcuts import render
from django.views import generic
from .models import Choice, Question

# Create your views here.

class DrillView(generic.DetailView):
    template_name = 'drill.html'

class AnswerView(generic.DetailView):
    template_name = 'answer.html'