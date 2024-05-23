from rest_framework import serializers
from .models import Cadastro, Carro, OrdemServico

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fileds = ["id", "name", "address", "pub_date"]
        exclude = []
        
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ["car", "plate", "idOwner"]
        exclude = []
        
class OrdemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = ["quantity", "description", "observation", "serviceDate", "total", "idPerson", "idCar"]
        exclude = []