from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Asset(models.Model):

    NOT_AVAILABLE = 'NA'
    AVAILABLE = 'AV'
    IN_USE = 'IU'

    STATUS_CHOICES = {
        NOT_AVAILABLE: 'Not Available',
        AVAILABLE: 'Available',
        IN_USE: 'In Use',
    }

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    borrowed_date = models.DateField(blank=True, null=True)
    returned_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return f'{self.vendor} _ {self.model}'

    

class Handover:
    pass
