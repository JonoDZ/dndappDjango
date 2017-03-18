from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from worldgen.dndGenerator import *
# Create your views here.

items = [

]

def returnFormSelection(uncleanedDjangoForm):
    #check if the form is valid
    if uncleanedDjangoForm.is_valid():
        #clean the form data
        cleanedDjangoForm = uncleanedDjangoForm.cleaned_data
        #create an empty array to store the selected results
        cleanedDjangoFormSelected = []
        #itereate returned fields in the form
        for field in cleanedDjangoForm:
            #if the checkbox was ticked
            if cleanedDjangoForm[field]:
                #add to array
                cleanedDjangoFormSelected.insert(0,field)
        #return the array
        return cleanedDjangoFormSelected
    #if form isnt valid
    else:
        return "form isnt valid"

def index(request):

    if request.method == 'POST':

        #process the form and get selected options
        selectedBuildings = returnFormSelection(GenOptionsBuildings(request.POST))
        selectedNpcs = returnFormSelection(GenOptionsNpcs(request.POST))
        
        #for testing, stringify response and push to HTTPresp
        total = str(selectedBuildings) + str(selectedNpcs)
        return HttpResponse(total)

        # if a GET (or any other method) we'll create a blank form
    else:
        genBuildingsForm = GenOptionsBuildings()
        genNpcsForm = GenOptionsNpcs()

    characterList= genChar(0,10)
    buildingList = genBuilding()
    #buildingList=dndGenerator.genBuilding()

    context = {
    'charList': characterList,
    'buildingList': buildingList,
    'genBuildingsForm': genBuildingsForm,
    'genNpcsForm': genNpcsForm
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