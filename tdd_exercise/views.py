from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Puzzle, Entry, Clue
import random

# Create your views here.

class DrillView(generic.DetailView):
    model = Entry
    template_name = 'drill.html'

class AnswerView(generic.DetailView):
    model = Clue
    template_name = 'answer.html'

def drill(request):
    # should have input field to have an answer
    # incorrect answer redisplays the same clue and message answer is incorrect
    # correct answer should redirect to answer view
    # should have escape hatch to get out

    try:
        guess = request.GET['guess'].upper()
        answer = Clue.objects.filter(entry__entry_text=guess)
        if answer:
            answer[0].selected = False
            answer[0].save()
            return render(request, 'answer.html',{'clue':answer})
        else:
            return render(request, 'drill.html',{'incorrect':True,'clue':list(Clue.objects.filter(selected=True))[0].clue_text})
    except:
        clue = random.choice(list(Clue.objects.all()))
        clue.selected = True
        clue.save()
        return render(request, 'drill.html',{'clue':clue})


