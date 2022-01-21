from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from rest_framework import viewsets


class GameTemplate(TemplateView):
    template_name = "assets/board.html"
