from django import forms
from .models import *
def attrs(Race):
		return {'class': 'special', 'data-width': '100', 'data-size': 'small', 'data-toggle': 'toggle', 'name': Race, 'data-on': Race, 'data-off':Race}

class GenOptionsBuildings(forms.Form):

	dataWidth = '100'
	buildingInn = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Inn')))
	buildingBlacksmith = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Blacksmith')))
	buildingMagicWeps = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('MagicWeps')))
	buildingHolysite = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Holysite')))
	buildingStable = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Stable')))
	buildingAlchemist = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Alchemist')))
	buildingJeweler = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Jeweler')))
	buildingEnchanter = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Enchanter')))
class GenOptionsNpcs(forms.Form):

	
	npcTieling = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Tieling')))
	npcHuman = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Human')))
	npcHalforc = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('HalfOrc')))
	npcHalfing = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Halfling')))
	npcHalfelf = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('HalfElf')))
	npcGnome = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Gnome')))
	npcElf = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Elf')))
	npcDwarf = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Dwarf')))
	npcDragonborn = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('DragonBorn')))