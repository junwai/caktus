from django.db import models

# Create your models here.
from datetime import date

# published crossword puzzle
class Puzzle(models.Model):
    # optional
    title_text = models.CharField(max_length=255, blank=True)
    
    # required
    pub_date = models.DateTimeField('date published')
    byline_text = models.CharField(max_length=255)
    publisher = models.CharField(max_length=12)

    def __str__(self):
        return self.title_text

# the actual answer
class Entry(models.Model):

    # required and unique
    # needs to be in all caps, if given as lowercase convert to all caps
    entry_text = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.entry_text

# the clue of the puzzle
class Clue(models.Model):

    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    clue_text = models.CharField(max_length=512)
    selected = models.BooleanField(default=False)
    theme = False

    def __str__(self):
        return self.clue_text
