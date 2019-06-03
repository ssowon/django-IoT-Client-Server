from django.conf.urls import url
from django.urls import path
from .views import HomePageView, SearchResultsView
from . import views

urlpatterns = [
    url(r'^$', views.index),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]