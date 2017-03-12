from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from worldgen.dndGenerator import *
# Create your views here.

items = [

]

def index(request):

    characterList= genChar(0,10)
    buildingList = genBuilding()
    #buildingList=dndGenerator.genBuilding()

    context = {
    'charList': characterList,
    'buildingList': buildingList
    }
    return render(request, 'worldgen/index.html', context)

def shop(request):
    return HttpResponse("Here is the shop")


def update(request):

    """for item in items:
        print(item)
        building = Building_type.objects.get(pk=8)
        building.building_name_last_set.create(name=item)
    """
    return HttpResponse("updated: " + str(items))

def regenNpcs(request, npcsToGen):
    """
    npcQuant = request.args.get('npcQuant', 0, type=int)
        charList = request.args.get('charList', 0)
        charList = charList.split(",")
        charList.remove("")
        characterList=dndGenerator.genChar(charList, npcQuant)
    """
    characterList = genChar(0,int(npcsToGen))
    buildingList = genBuilding()
    context = {
        'charList': characterList,
        'buildingList': buildingList
    }
    return render(request, 'worldgen/index.html', context)
    #return jsonify(render_template('npctable.html', charList=characterList))
