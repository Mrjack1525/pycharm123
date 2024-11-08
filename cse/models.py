from django.db import models


# Create your models here.
class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.EmailField(primary_key = True)
    comments = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    class Meta:
        db_table="contactus"


