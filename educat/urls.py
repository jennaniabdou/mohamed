from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [

	path('', views.index),

	path('categories/', views.category, name='categories'),

	path('^(?P<query>[A-Z][a-z]+)/$', views.search),



]