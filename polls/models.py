import uuid
from django.db import models

class Eleve(models.Model):
    prenom = models.CharField( max_length=200, null=True) 
    nom = models.CharField( max_length=200, null=True) 
    def __str__(self):
        return self.nom
    
