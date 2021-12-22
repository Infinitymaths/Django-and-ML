from django.urls import path
from django.conf.urls.static import static
from .views import first, func, results,base,about,contact

urlpatterns = [
    path('', base, name='home'),
    path('404/', func, name='404'),
    path('results', results, name='results_show'),
    path('main',first,name='homepage'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    
    
    ]