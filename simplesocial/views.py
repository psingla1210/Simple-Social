from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class TestPageView(TemplateView):
    template_name = 'test.html'

class ThanksPageView(TemplateView):
    template_name = 'thanks.html'
