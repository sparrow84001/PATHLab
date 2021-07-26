from django.db import models

# Create your models here.
class emp(models.Model):
    exampleInputEmail1=models.EmailField()
    exampleInputPassword1=models.CharField(max_length=50)

    def __str__(self):
        return self.exampleInputEmail1
    
    class Meta:
        db_table="emp"