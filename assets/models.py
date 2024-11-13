from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Asset(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    borrowed_date = models.DateField(blank=True, null=True)
    returned_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.vendor} _ {self.model}'

    

class Handover:
    pass
