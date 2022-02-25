from django.shortcuts import render
from django.http import HttpResponse
from expenses.models import Summary, Detail

def index(request):
    total = Summary.objects.count()
    return HttpResponse(f"Hello, world. You're at the expenses index, and it has {total} records.")
