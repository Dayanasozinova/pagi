import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


CONTENT = [str(i) for i in range(10000)]


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    data = {}
    with open(settings.BUS_STATION_CSV, encoding= 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row['ID']] = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}

    context = {
        'bus_stations': data,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
