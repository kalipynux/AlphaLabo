from django.db import models
from django.contrib.auth.models import User
import uuid

# class Patients(models.Model):

class Patients(models.Model):
    PATIENT_SEXE = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    GROUP_SANGUIN = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    PIECES_IDENTITE = (
        ('CNI', 'Carte Nationale d\'Identité'),
        ('PAS', 'Passeport'),
        ('PER', 'Permis de Conduire'),
        ('AUT', 'Autre'),
    )
    nom_patient = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=PATIENT_SEXE)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    date_enregistrement = models.DateField()
    pieces_identite = models.CharField(max_length=3, choices=PIECES_IDENTITE)
    numero_identite = models.CharField(max_length=50)
    groupe_sanguin = models.CharField(max_length=3, choices=GROUP_SANGUIN)
    images = models.ImageField(upload_to='media/patient_images', blank=True)
    pieces_jointes = models.FileField(upload_to='media/patient_files', blank=True)
    def __str__(self):
        return self.nom_patient + ' ' + self.prenom
    
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
    
class Categories_Examents(models.Model):
    nom_categorie = models.CharField(max_length=250)
    def __str__(self):
        return self.nom_categorie
    
    class Meta:
        verbose_name = 'Categorie Exament'
        verbose_name_plural = 'Categories Examents'

class Examents(models.Model):
    nom_exament = models.CharField(max_length=520)
    categorie = models.ForeignKey(Categories_Examents, on_delete=models.PROTECT)
    prix = models.IntegerField()
    description = models.TextField()
    date_ajout = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    images = models.ImageField(upload_to='media/exament_images', blank=True)
    pieces_jointes = models.FileField(upload_to='media/exament_files', blank=True)
    quantite = models.PositiveIntegerField(default=0)  # Ajout du champ quantite

    class Meta:
        verbose_name = 'Exament'
        verbose_name_plural = 'Examents'

    def __str__(self):
        return self.nom_exament
    
    def status_facture_exament(self):
        if self.disponible:
            return 'green'
        else:
            return 'red'
        
    def formatted_prix(self):
        return f"${self.prix} HT"
    @property
    def formatted_prix(self):
        return f"${self.prix} HT"
    

        
class Analyses(models.Model):
    image = models.ImageField(upload_to='media/analyse_images', blank=True)
    patient = models.ForeignKey(Patients, on_delete=models.PROTECT)
    exament = models.ForeignKey(Examents, on_delete=models.PROTECT)
    facture = models.BooleanField(default=False)
    date_analyse = models.DateField(auto_now_add=True)
    prix = models.ForeignKey(Examents, on_delete=models.PROTECT, related_name='analyses_prix', editable=False, null=True, blank=True, default=1)  # Ajout d'une valeur par défaut
    pieces_jointes = models.FileField(upload_to='media/analyse_files', null=True, blank=True)

    def __str__(self):
        return f"{self.patient} {self.exament} {self.date_analyse} {self.prix} {self.facture} {self.pieces_jointes}"
    
    class Meta:
        verbose_name = 'Analyse'
        verbose_name_plural = 'Analyses'

    def status_fature_analyse(self):
        if self.facture :
            return 'Oui'
        else:
            return 'Non'
        
    def save(self, *args, **kwargs):
        if self.exament.quantite is not None and self.exament.quantite > 0:
            self.exament.quantite -= 1
            self.exament.save()
        else:
            raise ValueError("La quantité de l'examen ne peut pas être négative ou nulle.")
        super(Analyses, self).save(*args, **kwargs)

    @staticmethod
    def get_quantite_exament_par_patient(patient_id):
        analyses = Analyses.objects.filter(patient_id=patient_id)
        quantite_total = sum(analyse.exament.quantite for analyse in analyses)
        return quantite_total
        
class Factures(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.PROTECT)
    analyses = models.ForeignKey(Analyses, on_delete=models.PROTECT, related_name='factures_analyses')
    quantite = models.PositiveIntegerField()
    total = models.IntegerField(editable=False)
    payé = models.BooleanField(default=False)
    versement = models.IntegerField()
    balance = models.IntegerField(editable=False)
    date_facture = models.DateField(auto_now_add=True)
    pieces_jointes = models.FileField(upload_to='media/facture_files', null=True, blank=True)
    numero_facture = models.CharField(max_length=1000, editable=False)
    utilisateur = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Le reçu de {self.patient}"
    
    def status_facture(self):
        if self.payé:
            return 'green'
        else:
            return 'red'
    
    def status_balance(self):
        if self.balance > 0:
            return 'red'
        elif self.balance * 0.5:
            return 'orange'
        else:
            return
        
    def save(self, *args, **kwargs):
        # Calculer le total et la balance avant de sauvegarder
        self.total = self.analyses.exament.prix * self.quantite
        self.balance = self.total - self.versement
        # Générer le numéro de facture
        self.numero_facture = Factures.generate_numero_facture(self.patient.nom_patient)
        super(Factures, self).save(*args, **kwargs)

    def formatted_total(self):
        return f"${self.total} HT"
    
    def formatted_balance(self):
        return f"${self.balance} HT"

    def formatted_versement(self):
        return f"${self.versement} HT"
    

    @property
    def formatted_total(self):
        return f"${self.total} HT"
    
    @property
    def formatted_balance(self):
        return f"${self.balance} HT"

    @property
    def formatted_versement(self):
        return f"${self.versement} HT"
    
    @staticmethod
    def generate_numero_facture(patient_name):
        unique_id = uuid.uuid4().hex[:6].upper()
        return f"{patient_name[:3].upper()}-{unique_id}"
        
    class Meta:
        verbose_name = 'Facture'
        verbose_name_plural = 'Factures'

class Resultats(models.Model):
    analyse = models.ForeignKey(Analyses, on_delete=models.PROTECT)
    resultat = models.TextField()
    date_resultat = models.DateField(auto_now_add=True)
    images = models.ImageField(upload_to='media/resultat_images', blank=True, null=True)
    pieces_jointes = models.FileField(upload_to='media/resultat_files', null=True, blank=True)
    
    def __str__(self):
        return f"Résultat de l'analyse {self.analyse}"
    
    class Meta:
        verbose_name = 'Resultat'
        verbose_name_plural = 'Resultats'