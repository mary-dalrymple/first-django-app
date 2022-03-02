from django.shortcuts import render
from django.http import HttpResponse
from expenses.models import Summary, Detail

def index(request):
  total_summaries = Summary.objects.count()
  total_detail = Detail.objects.count()
  return HttpResponse(f"Hello, world. You're at the expenses index and there are {total_summaries} summary records and {total_detail} records in the database.")
