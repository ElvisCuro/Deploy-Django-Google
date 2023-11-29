
from django.urls import path, include,re_path
from django.contrib import admin
from django.shortcuts import render
from django.views.generic import TemplateView

def index_view(request):
    return render(request,'index.html')

urlpatterns = [
    path('',index_view,name='index'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^(?!static/).*$', TemplateView.as_view(template_name='index.html')),
]
