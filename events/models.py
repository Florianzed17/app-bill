from django.contrib.auth.models import User
from django.db import models


class event(models.Model):
    THEME_CHOICES = (
        ('festival', 'Festival'),
        ('theatre', 'Théâtre'),
        ('soiree_musicale', 'Soirée Musicale'),
        ('sport', 'Sport'),
        # Ajoutez d'autres choix de thème ici
    )
    id = models.AutoField(primary_key=True)  # Champ id avec auto-incrémentation
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images')
    date = models.DateField()
    theme = models.CharField(max_length=100, choices=THEME_CHOICES)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    pays = models.CharField(max_length=100, default='Your Default Country')
    ville = models.CharField(max_length=100, default='Your Default city')
