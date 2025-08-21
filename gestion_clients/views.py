from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.contrib import messages


# Create your views here.
def liste_clients(request):
    clients = Client.objects.all().order_by('-date_creation')
    return render(request, "gestion_clients/liste_clients.html", {"clients":clients})

def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Client ajouté avec succès !")
            return redirect('liste_clients')
        else:
            messages.error(request, "❌ Une erreur est survenue. Vérifiez les champs.")
    else:
        form = ClientForm()
    return render(request, 'gestion_clients/ajouter_client.html',{'form':form})

def modifier_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Client modifié avec succès !")
            return redirect('liste_clients')
        else:
            messages.error(request, "❌ Impossible de modifier le client.")
    else:
        form = ClientForm(instance=client)
    return render(request,'gestion_clients/modifier_client.html', {'form': form, 'client': client})

def supprimer_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.delete()
        messages.success(request, "🗑️ Client supprimé avec succès.")
        return redirect('liste_clients')
    return render(request, 'gestion_clients/supprimer_client.html', {'client': client})


