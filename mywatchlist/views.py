from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
data_mywatchlist = MyWatchListItem.objects.all()

def show_mywatchlist(request):
    watched_movie = 0
    unwatched_movie = 0
    message = ""

    for movie in data_mywatchlist:
        if (movie.watched):
            watched_movie += 1
        else:
            unwatched_movie += 1

    if (watched_movie >= unwatched_movie):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
    'mywatchlist':data_mywatchlist,
    'nama': 'Arina Aunaka',
    'npm': '2106638690',
    'message': message
    }
    return render(request, "mywatchlist.html", context)

def show_html(request):
    context = {
    'mywatchlist':data_mywatchlist,
    }
    return render(request, "show_html.html", context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_xml_by_id(request, id):
    data_mywatchlist = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_json_by_id(request, id):
    data_mywatchlist = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")