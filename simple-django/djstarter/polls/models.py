"""Polls."""
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Define attribute for Question."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Question text."""
        return self.question_text

    def was_published_recently(self):
        """Published recently."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """Define attribute for Choice."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Choice_text."""
        return self.choice_text
