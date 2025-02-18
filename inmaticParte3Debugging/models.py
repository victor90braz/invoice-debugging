from django.db import models

class InvoiceModel(models.Model):
    last_number = models.IntegerField(default=0)

