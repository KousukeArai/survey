from asyncio.log import logger
import logging
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views import generic
from .models import Grade, Questions
from config.settings import *
from django.urls import reverse
from urllib.parse import urlencode

logger = logging.getLogger(__name__)

class IndexListView(generic.ListView):
    template_name = "index.html"
    model = Grade

    def get_queryset(self):
        grades = Grade.objects.all()
        return grades
    


class QuestionsView(generic.FormView):
    template_name = "questions.html"
    #form_