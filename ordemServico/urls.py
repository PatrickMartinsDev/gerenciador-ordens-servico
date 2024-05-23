from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.home, name="home"
        ),
    path(
        "cadastro/", 
         views.CadastroListCreate.as_view(), 
         name="cadastro-view-create"
         ),
    path(
        "cadastro/<int:pk>/",
        views.CadastroRetrieveUpdateDestroy.as_view(),
        name="update",
    ),
    path(
        "cadastro/list/",
        views.CadastroList.as_view(),
        name="CadastroList",
    ),
    path(
        "carro/", 
         views.CarroListCreate.as_view(), 
         name="Carro-view-create"
         ),
    path(
        "carro/<int:pk>/",
        views.CarroRetrieveUpdateDestroy.as_view(),
        name="update",
    ),
    path(
        "carro/list/",
        views.CarroList.as_view(),
        name="CarroList",
    ),
    path(
        "ordemServico/", 
         views.OrdemServicoListCreate.as_view(), 
         name="OrdemServico-view-create"
         ),
    path(
        "ordemServico/<int:pk>/",
        views.OrdemServicoRetrieveUpdateDestroy.as_view(),
        name="update",
    ),
    path(
        "ordemServico/list/",
        views.OrdemServicoList.as_view(),
        name="OrdemServicoList",
    ),
]

