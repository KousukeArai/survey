from asyncio.log import logger
import logging
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views import generic
from .models import Grade, Questions
from config.settings import *
from django.urls import reverse
from urllib.parse import urlencode

class IndexView(generic.ListView):
    template_name = "index.html"
    model = Grade


class QuestionsView(generic.DetailView):
    template_name = "questions.html"