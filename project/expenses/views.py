from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from expenses.models import Summary, Detail

def index(request):
  total_summaries = Summary.objects.count()
  total_detail = Detail.objects.count()
  return render(request, 'expenses/index.html', context={'total_summaries': total_summaries, 'total_detail': total_detail})

def summary(request, summary_id):
  summary = get_object_or_404(Summary, id=summary_id)
  return render(request, 'expenses/summary.html', {'summary': summary})
  # where {'summary': summary} is a dictionary defining the key and value
  # this context passes in the python object
