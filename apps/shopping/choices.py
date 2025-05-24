from django.db import models


class Fuel(models.TextChoices):
    NONE = "0", "Nenhum"
    ELETRIC = "1", "Elétrico"
    ALCOHOL = "12", "Álcool"
    GASOLINE = "3", "Gasolina"
    DIESEL = "4", "Diesel"
