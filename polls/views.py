from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Estás en la app de Premios')


def detail(request, question_id):
    return HttpResponse("Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse("Estás viendo los resultados de la pregunta número {question_id}")


def vote(request, question_id):
    return HttpResponse("Estás votando la pregunta número {question_id}")
