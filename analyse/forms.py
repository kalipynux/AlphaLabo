from django.forms import ModelForm
from. models import *
from django import forms


from django import forms
from .models import Analyses

class AddAnalyse(forms.ModelForm):
    class Meta:
        model = Analyses
        fields = ['image', 'patient', 'exament', 'facture', 'pieces_jointes']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'exament': forms.Select(attrs={'class': 'form-control'}),
            'facture': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'pieces_jointes': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class AddExament(forms.ModelForm):
    class Meta:
        model = Examents
        fields = ['nom_exament', 'categorie', 'prix', 'description', 'disponible', 'images', 'pieces_jointes', 'quantite']
        widgets = {
            'nom_exament': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pieces_jointes': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class AddPatient(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['nom_patient', 'prenom', 'sexe', 'date_naissance', 'adresse', 'telephone', 'email', 'date_enregistrement', 'pieces_identite', 'numero_identite', 'groupe_sanguin', 'images', 'pieces_jointes']
        widgets = {
            'nom_patient': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_enregistrement': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pieces_identite': forms.Select(attrs={'class': 'form-control'}),
            'numero_identite': forms.TextInput(attrs={'class': 'form-control'}),
            'groupe_sanguin': forms.Select(attrs={'class': 'form-control'}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pieces_jointes': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
class AddFacture(forms.ModelForm):
    class Meta:
        model = Factures
        fields = ['patient', 'analyses', 'quantite', 'payé', 'versement', 'pieces_jointes', 'utilisateur']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'analyses': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'payé': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'versement': forms.NumberInput(attrs={'class': 'form-control'}),
            'pieces_jointes': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'utilisateur': forms.Select(attrs={'class': 'form-control'}),
        }

class AddCategorie(forms.ModelForm):
    class Meta:
        model = Categories_Examents
        fields = ['nom_categorie']
        widgets = {
            'nom_categorie': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddResultats(forms.ModelForm):
    class Meta:
        model = Resultats
        fields = ['analyse', 'resultat', 'images', 'pieces_jointes']
        widgets = {
            'analyse': forms.Select(attrs={'class': 'form-control'}),
            'resultat': forms.Textarea(attrs={'class': 'form-control'}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pieces_jointes': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }



