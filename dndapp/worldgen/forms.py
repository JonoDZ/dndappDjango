from django import forms
from .models import *
def attrs(Race):
		return {'class': 'special', 'data-width': '100', 'data-size': 'small', 'data-toggle': 'toggle', 'name': Race, 'data-on': Race, 'data-off':Race}

class GenOptionsBuildings(forms.Form):

	dataWidth = '100'
	Inn = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Inn')))
	Blacksmith = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Blacksmith')))
	MagicWeps = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('MagicWeps')))
	Holysite = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Holysite')))
	Stable = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Stable')))
	Alchemist = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Alchemist')))
	Jeweler = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Jeweler')))
	Enchanter = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Enchanter')))

class GenOptionsNpcs(forms.Form):

	#Race.objects.get(pk=1)
	#race = random.choice(Race.objects.all())

	#build character details
	#character['race'] = race

	Tiefling = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Tiefling')))
	Human = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Human')))
	Halforc = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('HalfOrc')))
	Halfing = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Halfling')))
	Halfelf = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('HalfElf')))
	Gnome = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Gnome')))
	Elf = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Elf')))
	Dwarf = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Dwarf')))
	Dragonborn = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('DragonBorn')))