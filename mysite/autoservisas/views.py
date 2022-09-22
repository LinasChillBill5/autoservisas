from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Automobilis, Automobilio_modelis, Uzsakymo_eilute, Uzsakymas, Paslauga
from django.core.paginator import Paginator

def index(request):
    num_uzsakymai_now = Uzsakymas.objects.filter(status__exact="v").count()
    num_uzsakymai_done = Uzsakymas.objects.filter(status__exact="a").count()
    num_paslaugu = Paslauga.objects.all().count()
    if num_paslaugu < 7 and num_uzsakymai_now < 3:
        p_s = "Vidutinis arba mazas serviso uzimtumas. Klientai laukiami!"
    else:
        p_s = "Nevaziuokit, meistrai perkrauti darbu, Nera vietu!"

    kontext = {"num_uzsakymai_now": num_uzsakymai_now,
               "num_paslaugu": num_paslaugu,
               "num_uzsakymai_done": num_uzsakymai_done,
               "p_s": p_s
               }

    return render(request, "index.html", context=kontext)


def automobiliai(request):
    autos = Automobilio_modelis.objects.all()
    kontext = {
        'automobiliai': autos
    }
    return render(request, 'autos.html', context=kontext)


class UzsakListView(generic.ListView):
    model = Uzsakymas
    paginate_by = 2
    template_name = "uzsak_list.html"


class UzsakDetailView(generic.DetailView):
    model = Uzsakymas
    template_name = "uzsak_detail.html"
