from django.db import models

# Create your models here.
from datetime import date
from email.iterators import body_line_iterator
from importlib.metadata import entry_points
from turtle import title

class Puzzle(models.Model):
    # optional
    title_text = models.CharField(max_length=255, blank=True)
    
    # required
    pub_date = models.DateTimeField('date published')
    byline_text = models.CharField(max_length=255)
    publisher = models.CharField(max_length=12)

class Entry(models.Model):

    # required and unique
    # needs to be in all caps, if given as lowercase convert to all caps
    entry_text = models.CharField(max_length=50, unique=True)

class Clue(models.Model):

    entry = Entry()
    puzzle = Puzzle()
    clue_text = models.CharField(max_length=512)
    theme = False