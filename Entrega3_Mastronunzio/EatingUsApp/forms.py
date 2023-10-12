from django import forms


class NuevaReview(forms.Form):
    nombre = forms.CharField()
    zona = forms.CharField()
    desc = forms.CharField()
    puntaje = forms.IntegerField()
    tarjcred = forms.BooleanField()


class BuscarReview(forms.Form):
    nombre = forms.CharField()
