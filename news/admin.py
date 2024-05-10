from django.contrib import admin
from .models import News

models = [News]
for i in models:
    admin.site.register(i)
