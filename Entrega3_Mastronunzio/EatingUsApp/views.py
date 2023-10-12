from django.shortcuts import render
from EatingUsApp.models import Brunch, Almuerzo, Merienda, Cena
from EatingUsApp.forms import NuevaReview, BuscarReview
from django.http import HttpResponse


def inicio(request):
    return render(request, "EatingUsApp/index.html")


def brunch(request):
    return render(request, "EatingUsApp/brunch.html")


def almuerzo(request):
    return render(request, "EatingUsApp/almuerzo.html")


def merienda(request):
    return render(request, "EatingUsApp/merienda.html")


def cena(request):
    return render(request, "EatingUsApp/cena.html")


def nuevaReview(request):
    if request.method == "POST":

        nueva_review = NuevaReview(request.POST)

        if nueva_review.is_valid():
            informacion = nueva_review.cleaned_data

            nuevo_brunch = Brunch(nombre=informacion["nombre"],
                                  zona=informacion["zona"],
                                  desc=informacion["desc"],
                                  puntaje=informacion["puntaje"],
                                  tarjeta=informacion["tarjcred"]
                                  )
            nuevo_brunch.save()
            return render(request, "EatingUsApp/index.html")

        if nueva_review.is_valid():
            informacion = nueva_review.cleaned_data
            nuevo_almuerzo = Almuerzo(nombre=informacion["nombre"],
                                      zona=informacion["zona"],
                                      desc=informacion["desc"],
                                      puntaje=informacion["puntaje"],
                                      tarjeta=informacion["tarjcred"]
                                      )
            nuevo_almuerzo.save()
            return render(request, "EatingUsApp/index.html")

        if nueva_review.is_valid():
            informacion = nueva_review.cleaned_data
            nuevo_merienda = Merienda(nombre=informacion["nombre"],
                                      zona=informacion["zona"],
                                      desc=informacion["desc"],
                                      puntaje=informacion["puntaje"],
                                      tarjeta=informacion["tarjcred"]
                                      )
            nuevo_merienda.save()
            return render(request, "EatingUsApp/index.html")

        if nueva_review.is_valid():
            informacion = nueva_review.cleaned_data
            nuevo_cena = Cena(nombre=informacion["nombre"],
                              zona=informacion["zona"],
                              desc=informacion["desc"],
                              puntaje=informacion["puntaje"],
                              tarjeta=informacion["tarjcred"]
                              )
            nuevo_cena.save()
            return render(request, "EatingUsApp/index.html")

    else:
        nueva_review = NuevaReview()

    return render(request, "EatingUsApp/nueva_review.html", {"nueva_review": nueva_review})


def buscar(request):
    if request.method == "POST":

        nueva_review = BuscarReview(request.POST)

        if nueva_review.is_valid():
            informacion = nueva_review.cleaned_data

            nuevos_brunch = Brunch.objects.filter(
                zona__icontains=informacion["nombre"])
            return render(request, "EatingUsApp/lista.html", {"nuevos_brunch": nuevos_brunch})

    else:
        nueva_review = BuscarReview()

    return render(request, "EatingUsApp/mostrar_review.html", {"nueva_review": nueva_review})


def mostrar(request):
    pass
