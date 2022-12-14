from email.policy import default
from random import choices
from tkinter.tix import Tree
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.contrib.auth.models import User
from django import forms
import datetime

# Create your models here.

class StartUserWeightAndHeight(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ime = models.CharField(max_length=25, default="",
    validators=[MinLengthValidator(3)]
    )
    pocetna_tezina = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(400),
            MinValueValidator(45)
        ]
    )
    visina = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(250),
            MinValueValidator(140)
        ]
    )

    pol_m = "Muški"
    pol_z = "Ženski"
    polovi = [
        (pol_m,"Muški"),
        (pol_z,"Ženski")
    ]
    pol = models.CharField(max_length=6, choices=polovi,default=pol_m)

    def __str__(self):
        return self.ime + " - Pocetna tezina i visina"
    
    def get_absolute_url(self):
        return "/overview"
    


class CurrentWeight(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    trenutna_tezina = models.IntegerField(
              default=0,
        validators=[
            MaxValueValidator(400),
            MinValueValidator(45)
        ]
    )
    detalji = models.TextField(blank=True)
    class Meta:
       ordering = ['-date_added']
    def __str__(self):
        return f"Datum: {datetime.datetime.strftime(self.date_added, '%d-%b-%Y')} Tezina: {self.trenutna_tezina}kg"
    def get_absolute_url(self):
        return "/overview/weightlist"




    