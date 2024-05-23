from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cadastro, Carro, OrdemServico
from .serializers import CadastroSerializer, CarroSerializer, OrdemServicoSerializer
from rest_framework.views import APIView

def home(request):
    return render(request, "home.html")

class CadastroListCreate(generics.ListCreateAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    
    def delete(self, request, *args, **kwargs):
        Cadastro.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CadastroRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    lookup_field= "pk"
    
class CadastroList(APIView):
    def get(self, request, format=None):
        # Get the name from the query parameters (if none, default to empty string)
        name = request.query_params.get("name", "") 
       
        if name:
            # Filter the queryset based on the name
            cadastro = Cadastro.objects.filter(name__icontains=name)
        else:
            # If no name is provided, return all cadastros
            cadastro = Cadastro.objects.all()
        
        serializer = CadastroSerializer(cadastro, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# Carro classes
class CarroListCreate(generics.ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    
    def delete(self, request, *args, **kwargs):
        Carro.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CarroRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    lookup_field= "pk"
    
class CarroList(APIView):
    def get(self, request, format=None):
        # Get the name from the query parameters (if none, default to empty string)
        name = request.query_params.get("name", "") 
       
        if name:
            # Filter the queryset based on the name
            carro = Carro.objects.filter(name__icontains=name)
        else:
            # If no name is provided, return all Carros
            carro = Carro.objects.all()
        
        serializer = CadastroSerializer(carro, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Ordem de Serviço classes
class OrdemServicoListCreate(generics.ListCreateAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    
    def delete(self, request, *args, **kwargs):
        OrdemServico.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OrdemServicoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    lookup_field= "pk"
    
class OrdemServicoList(APIView):
    def get(self, request, format=None):
        # Get the name from the query parameters (if none, default to empty string)
        name = request.query_params.get("name", "") 
       
        if name:
            # Filter the queryset based on the name
            ordemServico = OrdemServico.objects.filter(name__icontains=name)
        else:
            # If no name is provided, return all OrdemServicos
            ordemServico = OrdemServico.objects.all()
        
        serializer = CadastroSerializer(ordemServico, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    