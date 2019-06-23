from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
# import myapp.dataFile
from myapp.dataFile import data
from myapp.models import Place


def index(request):
    polish = request.GET.get('polish', '')
    vegetarian = request.GET.get('vegetarian', '')
    asian = request.GET.get('asian', '')
    newData = []
    active = ''
    if polish:
        active = 'polish'
        for i in data:
            kinds = i['kinds']
            isPolish = list(filter(lambda x: x['name'] == "polish", kinds))
            if len(isPolish) > 0:
                newData.append(i)
    elif vegetarian:
        active = 'vegetarian'
        for i in data:
            types = i['types']
            isVegetarian = list(
                filter(lambda x: x['name'] == "vegetarian", types))
            if len(isVegetarian) > 0:
                newData.append(i)
    elif asian:
        active = 'asian'
        for i in data:
            kinds = i['kinds']
            isAsian = list(filter(lambda x: x['name'] == "asian", kinds))
            if len(isAsian) > 0:
                newData.append(i)
    else:
        newData = data

    return render(request, 'tpl/index.html', {
        'data': newData,
        'active': active
    })


def place_model(request):
    places = Place.objects.all()
    return render(request, 'tpl/place_model.html', {'places': places})


def listy(request):
    data = ['Arbuz', 'Bakłażan', 'Pomarańcza', 'Jabłko']
    newData = data[:]
    newData.append('Truskawki')
    newData.append('Śliwki')
    newData.append('Marchewka')
    newData.append('Winogrona')
    newData.append('Malina')
    newData.extend(['Pietruszka', 'Ciecierzyca', 'Wanilia'])
    sortData = newData[:]
    sortData.sort()

    return render(request, 'tpl/listy.html', {
        'data': data,
        'newData': newData,
        'sortData': sortData

    })


def slowniki(request):
    rosliny = {
        "Jabłko": "owoc",
        "Marchew": "warzywo",
        "Pomidor": "warzywo",
        "Ogorek": "warzywo",
        "Pietruszka": "warzywo",
        "Melon": "owoc",
        "Truskawki": "owoc",
        "Jagody": "owoc",

    }

    return render(request, 'tpl/slowniki.html', {
        'data': rosliny
    })


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
