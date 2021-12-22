from django.urls import path
from django.conf.urls.static import static
from polls import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='homepage'),
    path('home',views.sentiment,name='home'),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact")
] 
