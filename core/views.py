from multiprocessing.managers import BaseManager
from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import redirect, render

from core.models import Person


# Create your views here.
def home(request: Request) -> HttpResponse:
    persons: BaseManager[Person] = Person.objects.all()

    return render(request, 'index.html', {'persons': persons})


def save(request: Request) -> HttpResponse:
    vname = request.POST.get('name')

    Person.objects.create(name=vname)
    persons = Person.objects.all()

    return render(request, 'index.html', {'persons': persons})


def edit(request: Request, id: int) -> HttpResponse:
    person = Person.objects.get(id=id)

    return render(request, 'update.html', {'person': person})


def update(request: Request, id: int) -> HttpResponse:
    vname = request.POST.get('name')
    person = Person.objects.get(id=id)

    person.name = vname
    person.save()

    return redirect(home)


def delete(request: Request, id: int) -> HttpResponse:
    former_person = Person.objects.get(id=id)
    former_person.delete()

    print(former_person)

    return redirect(home)
