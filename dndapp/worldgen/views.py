from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from worldgen.dndGenerator import genChar
# Create your views here.
names = [

]
def index(request):

    #for name in names:
     #   gnome_last_name(name=name).save()
    lastestHumanNames = Human_male_name.objects.order_by('name')[:5]
    output = ', '.join([name.name for name in lastestHumanNames])

    characterList= genChar(0,10)
    #buildingList=dndGenerator.genBuilding()

    context = {'charList': characterList}
    return render(request, 'worldgen/index.html', context)

def shop(request):
    return HttpResponse("Here is the shop")