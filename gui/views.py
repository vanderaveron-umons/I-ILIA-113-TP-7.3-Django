from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from gui.models import Client, Commande, Detailscommande, Produit

class ClientDetail(DetailView):
    model = Client
    template_name = "gui/detail_client.html"
    
class ClientUpdate(UpdateView):
    model = Client
    fields = ['adresse', 'codepostal', 'ville', 'email',]
    template_name = "gui/update_client.html"
    success_url = reverse_lazy('clients_list') 

class ClientList(ListView):
    model = Client
    template_name = 'gui/lister_clients.html'
    
class ClientCreate(CreateView):
    model = Client
    fields = ['nom', 'prenom', 'adresse', 'codepostal', 'ville', 'email',]
    template_name = 'gui/ajouter_client.html'
    success_url = reverse_lazy('clients_list')

class ClientDelete(DeleteView):
    model = Client
    template_name = 'gui/supprimer_client.html'
    success_url = reverse_lazy('clients_list')
    


class CommandeList(ListView):
    model = Commande
    template_name = 'gui/lister_commandes.html'
    
class CommandeCreate(CreateView):
    model = Commande
    template_name = 'gui/ajouter_commande.html'
    fields = ['datec', 'commentaire', 'idclient']
    success_url = reverse_lazy('commandes_list')
    
class CommandeDelete(DeleteView):
    model = Commande
    template_name = 'gui/supprimer_commande.html'
    success_url = reverse_lazy('commandes_list')
    
    
class CommandeUpdate(UpdateView):
    model = Commande
    template_name = 'gui/update_commande.html'
    fields = ['commentaire']
    success_url = reverse_lazy('commandes_list')
   
class CommandeDetail(DetailView):
    model = Commande
    template_name = "gui/detail_commande.html"
   
   
class DetailsCommandeDetail(DetailView):
    model =  Detailscommande
    template_name = "gui/detail_detailscommande.html"
    
    
class ProduitDetail(DetailView):
    model = Produit
    template_name = "gui/detail_produit.html"
    

class ProduitList(ListView):
    model = Produit
    template_name = 'gui/lister_produits.html'
    
def example_view (request) :
    return HttpResponse (
    " Exemple d’une requete HTTP GET et sa reponse HTTP ",
    status = 200
    )
    
    
def add_view (request , operation) :
    result = eval (operation)
    context = {
        'OPERATION' : operation,
        'OPERATION_RESULT' : result,
    }
    return render (request , 'gui/add.html', context)
    
def home(request):
    return render (request , 'gui/home.html')