from django.db import models

class Cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.CharField(max_length=100)
    plate = models.CharField(max_length=7)
    idOwner = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    
class OrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    description = models.TextField()
    total = models.FloatField()
    observation = models.TextField()
    serviceDate = models.DateTimeField()
    idPerson = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    idCar = models.ForeignKey(Carro, on_delete=models.CASCADE)
