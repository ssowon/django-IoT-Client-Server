from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Sensorvalue
import sqlite3

def index(request):
    conn=sqlite3.connect('light.sqlite3')
    c=conn.cursor()

    datelist = []
    cdslist = []
    for row in c.execute('SELECT * FROM LIGHT'):
        datelist.append(row)

    sensorvalues = Sensorvalue.objects.all()
    context = {'dates': datelist}

    # context에 모든 센서 정보를 저장
    return render(request, 'searchdb/index.html', context)
    # context안에 있는 센서 정보를 index.html로 전달

class HomePageView(TemplateView):
    template_name = 'searchdb/index.html'


class SearchResultsView(ListView):
    model = Sensorvalue
    template_name = 'searchdb/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Sensorvalue.objects.filter(
            Q(datein__icontains=query) | Q(cds__icontains=query)
        )
        return object_list
