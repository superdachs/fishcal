from django.shortcuts import render
from fisherman.models import Catch
from fish.models import Fish
import datetime

def Highscore(request):
    catches = Catch.objects.filter(date__year=datetime.datetime.now().year)
    fishes = Fish.objects.all()
    context = {}

    catchlists = []
    for fish in fishes:
        fish_catches = catches.filter(fish=fish).order_by('size')
        l = []
        for catch in fish_catches:
            l.append(catch)

        catchlists.append([fish, l])
        print(l)
    context.update({'catches': catchlists})
    print(context)

    return render(request, 'highscore.html', context)