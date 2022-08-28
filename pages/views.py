from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class AboutUs(TemplateView):
    template_name = "pages/about_us.html"
