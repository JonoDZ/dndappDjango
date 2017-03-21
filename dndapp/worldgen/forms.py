from django import forms
from .models import *
from random import randint
def attrs(Race):
		return {'class': 'special', 'data-width': '100', 'data-size': 'small', 'data-toggle': 'toggle', 'name': Race, 'data-on': Race, 'data-off':Race}

class GenOptionsSeed(forms.Form):
	seed = forms.IntegerField(label ='', min_value=1, max_value=1000000, required=False, widget=forms.NumberInput())

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

	Tiefling = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Tiefling')))
	Human = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Human')))
	HalfOrc = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('HalfOrc')))
	Halfling = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Halfling')))
	HalfElf = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('HalfElf')))
	Gnome = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Gnome')))
	Elf = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Elf')))
	Dwarf = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('Dwarf')))
	Dragonborn = forms.BooleanField(label ='', initial=True, required=False, widget=forms.CheckboxInput(attrs=attrs('DragonBorn')))

class GenOptionsNpcsQuant(forms.Form):
	npcQuant = forms.IntegerField(label ='', min_value=1, initial=10, max_value=100, required=False, widget=forms.NumberInput(attrs=attrs({'id': 'rerollBtn', 'size':'5'})))