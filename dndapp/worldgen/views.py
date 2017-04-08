from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
import random
from worldgen.dndGenerator import *
# Create your views here.
# import pdb; pdb.set_trace()
items = [

]

def returnFormSelection(uncleanedDjangoForm):
    #check if the form is valid
    if uncleanedDjangoForm.is_valid():
        cleanedDjangoFormSelected = []
        cleanedDjangoForm = uncleanedDjangoForm.cleaned_data
        for field in cleanedDjangoForm:
            if cleanedDjangoForm[field]:
                cleanedDjangoFormSelected.insert(0,field)
       
        return cleanedDjangoFormSelected
    #if form isnt valid
    else:
        return "form isnt valid"

newSeed = random.random()

def index(request):
    newSeed = random.random()
    if request.method == 'POST':
        #process the form and get selected options
        seed =GenOptionsSeed(request.POST)
        selectedBuildings = returnFormSelection(GenOptionsBuildings(request.POST))
        selectedNpcs = returnFormSelection(GenOptionsNpcs(request.POST))      
        quantNpcs = GenOptionsNpcsQuant(request.POST)
        #will find if max value is exceded (umoung other things)
        """
        if seed.is_valid():
            if seed['seed'].data:
                newSeed= int(seed['seed'].data)
            else:
                newSeed = randint(0,9999)
        """
        if quantNpcs.is_valid():
            quantNpcs = quantNpcs['npcQuant'].data
            characterList= genChar(selectedNpcs, int(quantNpcs), newSeed)
        else:
            characterList= genChar(selectedNpcs, 10, newSeed)
       
        buildingList = genBuilding()

    # Non-POST form submitted page:
    else:   
        characterList= genChar(0,10)
        buildingList = genBuilding()
        drinksList = genDrinks()

    genSeedForm = GenOptionsSeed(initial={'seed': newSeed})
    genBuildingsForm = GenOptionsBuildings()
    genNpcsForm = GenOptionsNpcs()
    genNpcsQuantForm = GenOptionsNpcsQuant()

    context = {
    ## form variables
    'charList': characterList,
    'buildingList': buildingList,
    ## forms
    'genSeedForm': genSeedForm,
    'genBuildingsForm': genBuildingsForm,
    'genNpcsForm': genNpcsForm,
    'genNpcsQuantForm': genNpcsQuantForm,
    ##building details
    'drinkNames' : drinksList
    }

    return render(request, 'worldgen/index.html', context)

def shop(request):
    return HttpResponse("Here is the shop")

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse(form.fields)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'worldgen/names.html', {'form': form})