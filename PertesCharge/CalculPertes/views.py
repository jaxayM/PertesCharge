from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import script

def index(request):
    form = forms.Input()
    return render(request, "CalculPertes/index.html",{'form':form})

def form_view(request):
    form = forms.Input()

    if request.method == 'POST':
        form = forms.Input(request.POST)

        if form.is_valid():
            D = form.cleaned_data['diametre']
            L = form.cleaned_data['longeur']
            e = form.cleaned_data['rugosite']
            Q = form.cleaned_data['debit']
            mu = form.cleaned_data['viscosite']
            ro = form.cleaned_data['massevol']
            R, deltaP = script.programme(D,L,e,Q,mu,ro)

            return HttpResponse("Reynolds: "+str(R)+"</br>Pertes de charge: "+str(deltaP)+" Pa") #test
    return render(request, 'CalculPertes/index.html',{'form':form})
