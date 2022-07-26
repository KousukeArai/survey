from asyncio.log import logger
import logging
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views import generic
# from .models import Grade, Questions
from config.settings import *
from django.urls import reverse
from urllib.parse import urlencode

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"


class Grade1View(generic.TemplateView):
    template_name = "grade1.html"


class Grade2View(generic.TemplateView):
    template_name = "grade2.html"


class Grade3View(generic.TemplateView):
    template_name = "grade3.html"


class Question1View(generic.TemplateView):
    template_name = "questions.html"


class Question2View(generic.TemplateView):
    template_name = "questions.html"


class Question3View(generic.TemplateView):
    template_name = "questions.html"


# class ResultView(generic.ListView):
#     template_name = "result.html"
#     def get(self, request):
#         base = request.GET.get('base')
#         gender = request.GET.get('gender')
#         #URLからbase取得
#         context = {}
#         context["base"] = Base_type.objects.filter(id=base).first()
#         context["colors"] = Colors.objects.filter(base_type=base)
#         if int(gender) <= 2:
#             context["items"] = Items.objects.filter(color__base_type__id=base, gender=gender)
#         else:
#             context["items"] = Items.objects.filter(color__base_type__id=base).all()
        
#         return render(request, 'result.html', context)