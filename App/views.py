from django.shortcuts import render
from django.http import HttpResponse
from .models import compliments
import random
from django.forms import formset_factory
from .forms import Form

def compliment(request):
    all_com = compliments.objects.all()

    if all_com.exists():
        random_com = random.choice(all_com)
        display = random_com.text

    else:
        display = " No compliments in the data base "

    context = {'random_key': display}
    return render(request, "comp.html", context)


def Form_view(request):
    form = formset_factory(Form, extra=2)
    if request.method=="POST":
        formset = form(request.POST)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)
    else:
        formset = form()

    return render(request, 'form.html', {'f': formset})