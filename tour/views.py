from django.shortcuts import render, get_object_or_404
from tour.models import Tours
from category.models import Category


# Create your views here.
def tours(request, category_slug=None):
    categories = None
    tour = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        tour = Tours.objects.filter(category=categories)
    else:
        tour = Tours.objects.all()

    context = {'tour': tour}
    return render(request, 'includes/tours.html', context)


def tour_detail(request, category_slug, tour_slug):
    try:
        single_tour = Tours.objects.get(category__slug=category_slug, slug=tour_slug)
    except Exception as e:
        raise e

    context = {'single_tour': single_tour}
    return render(request, 'includes/tour_detail.html', context)
