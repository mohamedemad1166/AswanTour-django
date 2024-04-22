from django.shortcuts import render
from tour.models import Tours


def home(request):
    tour = Tours.objects.all()
    context = {'tour': tour}
    return render(request, 'index.html', context)


