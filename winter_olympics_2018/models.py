from django.db import models

# Create your models here.


class Country(models.Model):

    class Meta:
        '''Plural name for Country'''
        verbose_name_plural = "Countries"

    def __str__(self):
        '''string representaion of model object'''
        return str(self.rank)+". "+self.noc + " ("+self.short+")"

    rank = models.IntegerField()
    noc = models.CharField(max_length=255)
    gold = models.IntegerField()
    silver = models.IntegerField()
    bronze = models.IntegerField()
    total = models.IntegerField()
    short = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)