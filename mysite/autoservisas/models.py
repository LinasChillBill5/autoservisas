from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class Automobilio_modelis(models.Model):
    # id = models.Field(primary_key=True, help_text="Automobilio modelio ID")
    marke = models.CharField("Automobilio marke", max_length=100)
    modelis = models.CharField("Automobilio modelis", max_length=100)
    metai = models.CharField("Pagaminimo metai", max_length=10)

    def __str__(self):
        return f"{self.marke} {self.modelis} {self.metai}"

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobilio modeliai"


class Automobilis(models.Model):
    # id = models.Field(primary_key=True, help_text="unikalus ID Kiekvienam Automobiliui")
    valstyb_nr = models.CharField(help_text="Iveskite Valstyb. Numeri", max_length=20)
    automobilio_modelis_ID = models.ForeignKey("Automobilio_modelis", on_delete=models.SET_NULL, null=True)
    vin_kodas = models.CharField("Vin kodas", blank=False, max_length=50)
    klientas = models.CharField("Vardas, Pavarde", max_length=100)

    def __str__(self):
        return f"{self.valstyb_nr} {self.vin_kodas} {self.klientas}"

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"


class Uzsakymas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="unikalus ID Kiekvienam Uzsakymui")
    data = models.DateField(help_text="Iveskite Data")
    automobilis_ID = models.ForeignKey("Automobilis", on_delete=models.SET_NULL, null=True)
    suma = models.CharField("Kaina Viso:", blank=False, max_length=20)

    def __str__(self):
        return f"{self.data} {self.suma}"

    class Meta:
        verbose_name = "Uzsakymas"
        verbose_name_plural = "Uzsakymai"

    UZSAKYMO_STATUSAS = (
        ("x", "Administratorius"),
        ("p", "Priimta, dar nevykdoma"),
        ("v", "Vykdoma"),
        ("a", "Atlikta"),
    )

    status = models.CharField(max_length=1, choices=UZSAKYMO_STATUSAS, blank=True, default="x", help_text="Statusas")


class Uzsakymo_eilute(models.Model):
    # id = models.Field(primary_key=True, default=uuid.uuid4, help_text="unikalus ID Kiekvienai Uzsakymo eil.")
    paslauga = models.ForeignKey("Paslauga", on_delete=models.SET_NULL, null=True)
    uzsakymas = models.ForeignKey("Uzsakymas", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis")
    kaina = models.FloatField("Kaina")

    def __str__(self):
        return f"{self.kiekis} {self.kaina}"

    class Meta:
        verbose_name = "Užsakymo eilutė"
        verbose_name_plural = "Užsakymo eilutės"


class Paslauga(models.Model):
    # id = models.Field(primary_key=True, default=uuid.uuid4, help_text="Automobilio modelio ID")
    pavadinimas = models.CharField("Pavadinimas", max_length=100)
    kaina = models.FloatField("Kaina")

    def __str__(self):
        return f"{self.pavadinimas} {self.kaina}"

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"


