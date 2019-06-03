from django.shortcuts import render
from django.http import HttpResponse
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
