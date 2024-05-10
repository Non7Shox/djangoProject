from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from news.models import News


class NewsView(TemplateView):
    def get(self, request):
        context = {}
        news = News.objects.all()
        context['news'] = news
        return render(request, 'news.html', context)


class NewsDetailView(DetailView):
    template_name = 'detail.html'


def detail_view(request, pk):
    news = News.objects.filter(id=pk)
    return render(request, 'detail.html', {'data': news})
