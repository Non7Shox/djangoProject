from django.urls import path

from .views import NewsView, detail_view


urlpatterns = [
    path('list/', NewsView.as_view(), name='news'),
    path('detail/<int:pk>/', detail_view, name='detail'),
]