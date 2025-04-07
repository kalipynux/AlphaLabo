from django.views.generic import ListView,CreateView
from .models import *
from.forms import *
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.urls import reverse_lazy

# Vue pour afficher les analyses
class Affichage(ListView):
    template_name = 'home.html'
    model = Analyses
    context_object_name = 'analyses'
    queryset = Analyses.objects.all()


# Vue pour afficher les patients
class Affichage(ListView):
    template_name = 'patient.html'
    model = Patients
    context_object_name = 'patients'
    queryset = Patients.objects.all()

# class pour ajouter les analyse

class AddAnalyses(CreateView):

    #utilisations du model
    model = Analyses
    #pointage du formulaire
    form_class = AddAnalyse
    # Affichage du templates
    template_name = 'add_analyse_form.html'
    #redirection apres enrefistrement
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Enregistrement de l'analyse
        form.save()
        messages.success(self.request, "Analyse ajoutée avec succès.")
        return super().form_valid(form)
    def form_invalid(self, form):
        # En cas d'erreur de validation du formulaire
        messages.error(self.request, "Erreur lors de l'ajout de l'analyse.")
        return super().form_invalid(form)
    
# class pour ajouter les examens
class AddExament(CreateView):
    # Utilisation du model
    model = Examents
    # Pointage du formulaire
    form_class = AddExament
    # Affichage du templates
    template_name = 'add_exament_form.html'
    # Redirection apres enregistrement
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Enregistrement de l'examen
        form.save()
        messages.success(self.request, "Examen ajouté avec succès.")
        return super().form_valid(form)
    def form_invalid(self, form):
        # En cas d'erreur de validation du formulaire
        messages.error(self.request, "Erreur lors de l'ajout de l'examen.")
        return super().form_invalid(form)
    

class AddPatient(CreateView):
    # Utilisation du model
    model = Patients
    # Pointage du formulaire
    form_class = AddPatient
    # Affichage du templates
    template_name = 'add_patient_form.html'
    # Redirection apres enregistrement
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Enregistrement de l'examen
        form.save()
        messages.success(self.request, "Patient ajouté avec succès.")
        return super().form_valid(form)
    def form_invalid(self, form):
        # En cas d'erreur de validation du formulaire
        messages.error(self.request, "Erreur lors de l'ajout du patient.")
        return super().form_invalid(form)
    
class AddFacture(CreateView):
    # Utilisation du model
    model = Factures
    # Pointage du formulaire
    form_class = AddFacture
    # Affichage du templates
    template_name = 'add_facture_form.html'
    # Redirection apres enregistrement
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Enregistrement de l'examen
        form.save()
        messages.success(self.request, "Facture ajoutée avec succès.")
        return super().form_valid(form)
    def form_invalid(self, form):
        # En cas d'erreur de validation du formulaire
        messages.error(self.request, "Erreur lors de l'ajout de la facture.")
        return super().form_invalid(form)
    
class AddCategorie(CreateView):
    # Utilisation du model
    model = Categories_Examents
    # Pointage du formulaire
    form_class = AddCategorie
    # Affichage du templates
    template_name = 'add_categorie_form.html'
    # Redirection apres enregistrement
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Enregistrement de l'examen
        form.save()
        messages.success(self.request, "Catégorie ajoutée avec succès.")
        return super().form_valid(form)
    def form_invalid(self, form):
        # En cas d'erreur de validation du formulaire
        messages.error(self.request, "Erreur lors de l'ajout de la catégorie.")
        return super().form_invalid(form)
    
# class pour ajouter les resultats
class AddResultat(CreateView):
    # Utilisation du model
    model = Resultats
    # Pointage du formulaire
    form_class = AddResultats
    # Affichage du templates
    template_name = 'add_resultat_form.html'
    # Redirection apres enregistrement
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        # Enregistrement de l'examen
        form.save()
        messages.success(self.request, "Résultat ajouté avec succès.")
        return super().form_valid(form)
    def form_invalid(self, form):
        # En cas d'erreur de validation du formulaire
        messages.error(self.request, "Erreur lors de l'ajout du résultat.")
        return super().form_invalid(form)


#fonction de modification
def modifier(request, id):
    analyse = get_object_or_404(Analyses, id=id)
    patients = Patients.objects.all()
    examents = Examents.objects.all()
    
    if request.method == 'POST':
        form = AddAnalyse(request.POST, request.FILES, instance=analyse)
        if form.is_valid():
            form.save()
            messages.success(request, "L'analyse a bien été modifiée.")
            return redirect("home")
    else:
        form = AddAnalyse(instance=analyse)
    
    return render(request, "modifanalyse.html", {'form': form, 'patients': patients, 'examents': examents})




# def modifier(request, id):
#     analyse = get_object_or_404(Analyses, id=id)
#     patients = Patients.objects.all()
#     examents = Examents.objects.all()
#     errors = {}

#     if request.method == 'POST':
#         image = request.FILES.get('image')
#         patient_id = request.POST.get('patient')
#         exament_id = request.POST.get('exament')
#         facture = request.POST.get('facture')
#         date_analyse = request.POST.get('date_analyse')
#         prix = request.POST.get('prix')
#         pieces_jointes = request.POST.get('pieces_jointes')

#         # validations
#         if not patient_id:
#             errors['patient'] = "Le patient est obligatoire."

#         if not exament_id:
#             errors['exament'] = "L'exament est obligatoire."

#         if not facture:
#             errors['facture'] = "L'analyse doit être facturée."

#         if not date_analyse:
#             errors['date_analyse'] = "Préciser la date."

#         if not prix:
#             errors['prix'] = "Le prix doit être précisé."

#         if not pieces_jointes:
#             errors['pieces_jointes'] = "Sélectionner une pièce jointe."

#         if not errors:
#             patient = get_object_or_404(Patients, id=patient_id)
#             exament = get_object_or_404(Examents, id=exament_id)
#             analyse.patient = patient
#             analyse.exament = exament
#             analyse.facture = facture
#             analyse.date_analyse = date_analyse
#             analyse.prix = prix
#             analyse.pieces_jointes = pieces_jointes

#             if image:
#                 fs = FileSystemStorage()
#                 filename = fs.save(image.name, image)
#                 analyse.image = fs.url(filename)

#             analyse.save()
#             messages.success(request, "L'analyse a bien été modifiée.")
#             return redirect("home")
#         else:
#             for key, error in errors.items():
#                 messages.error(request, error)

#     return render(request, "modifanalyse.html", {'analyse': analyse, 'patients': patients, 'examents': examents, 'errors': errors})