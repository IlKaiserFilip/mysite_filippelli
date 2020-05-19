"""mysite_filippelli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
#La funzione path serve ad inserire un percorso tramite il quale si visualizzerà la pagina creata.
#La funzione path ha 4 argomenti:
#1)Route:una stringa che contiene un pattern UR. Non cerca GET o POST. In https://127.0.0.1:8000/polls il polls/ è la parte della route;
#2)View:Quando trova la route chiama una funzione con una HttpRequest con i valori trovati come keyword;
#3)Kwargs:Keyword arguments che possono essere passati alla view;
#4)Name:dare un nome all'URL per distinguerlo.

#migrate: comando che prende tutte le migrazioni che non sono state applicate e le esegue sul database sincronizzando le modifiche apportate ai modelli con lo schema nel database.
#sqlmigrate: comando che in realtà non esegue la migrazione sul database, ma lo stampa sullo schermo in modo da poter vedere ciò che SQL Django ritiene necessario. Serve per vedere cosa farà Django/ se ci sono amministratori nel db che richiedono SQL per modifiche
#Quando abbiamo fatto il collegamento alla domanda in polls/index.html il collegamento era parzialmente codificato,il problema è che divedta difficile poi cambiare URL nei progetti con molti template.Visto che abbiamo il name nel path() si puòusare il tag{% url %}
#Nei progetti Django "seri" si possono trovare 10 o 20 app allo stesso momento.Aggiungendo il namespase o dando il nome all'app si possono evitare problemi derivati da path simili o con nomi uguali
#request.POST:è un oggetto simile a un dizionario che consente di accedere ai dati inviati in base al nome della chiave.I valori sono sempre stringhe
#request.POST['choice']restituisce l'ID della scelta selezionata come stringa.La funzione aumenterà il valore KeyError se choice non è stato fornito nei dati POST.
#Dopo aver incrementato il conteggio delle scelte, il codice restituisce un valore HttpResponseRedirect invece di un HttpResponse.
#reverse():funzione nel HttpResponseRedirect constructor. Questa funzione evita di dover codificare un URL nella funzione di view. Ci viene dato il nome della view a cui vogliamo passare il controllo e la parte variabile del pattern URL che punta a quella vista.
