from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'main/base.html'


def homepage(request):
    return render(request, 'main/base.html')
