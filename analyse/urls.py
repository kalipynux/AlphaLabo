from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URL pour la page d'accueil
    path('', Affichage.as_view(), name='home'),

    path('patient/',Affichage.as_view(), name='patient'),

    path('add/', AddAnalyses.as_view(), name='add'),

    path('modifanalyse/<int:id>/',modifier, name='modif'),

    path('add_exament/', AddExament.as_view(), name='add_exament'),
    # URL pour la page d'ajout de facture
    path('add_facture/', AddFacture.as_view(), name='add_facture'),
    # URL pour la page d'ajout de patient
    path('add_patient/', AddPatient.as_view(), name='add_patient'),
    # URL pour la page de résultats
    path('add_resultat/', AddResultat.as_view(), name='add_resultat'),
    # URL pour la page de détails d'une analyse
    path('add_categorie/', AddCategorie.as_view(), name='add_categorie'),

]
# Configuration pour servir les fichiers multimédias
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)