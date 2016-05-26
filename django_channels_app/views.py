from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def main(request):
    return HttpResponse(render(request, "index.html"))
