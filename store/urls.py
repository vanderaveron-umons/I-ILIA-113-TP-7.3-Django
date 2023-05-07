"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gui.views import example_view, add_view, home
from gui.views import ClientDetail, ClientList, ClientCreate, ClientDelete, ClientUpdate
from gui.views import CommandeDetail, CommandeList, CommandeCreate, CommandeDelete, CommandeUpdate
from gui.views import DetailsCommandeDetail
from gui.views import ProduitDetail, ProduitList

urlpatterns = [
    
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('example/', example_view ),
    path('add/<str:operation>/', add_view),
    path('clients/', ClientList.as_view(), name = 'clients_list'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='clients_detail'),
    path('clients/create/', ClientCreate.as_view(), name = 'clients_create'),
    path('clients/delete/<int:pk>/', ClientDelete.as_view(), name='clients_delete'),
    path('clients/update/<int:pk>/', ClientUpdate.as_view(), name='clients_update'),
    path('commandes/', CommandeList.as_view(), name = 'commandes_list'),
    path('commandes/<int:pk>', CommandeDetail.as_view(), name = 'commandes_detail'),
    path('commandes/create/', CommandeCreate.as_view(), name = 'commandes_create'),
    path('commandes/delete/<int:pk>/', CommandeDelete.as_view(), name = 'commandes_delete'),
    path('commandes/update/<int:pk>/', CommandeUpdate.as_view(), name = 'commandes_update'),
    path('detailscommande/<int:pk>/', DetailsCommandeDetail.as_view(), name='detailscommande_detail'),
    path('produits/', ProduitList.as_view(), name = 'produits_list'),
    path('produits/<int:pk>/', ProduitDetail.as_view(), name='produits_detail'),
]
