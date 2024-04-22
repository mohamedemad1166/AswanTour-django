from django.urls import path
from tour.views import tours, tour_detail, about
from contactform.views import contact

urlpatterns = [
    path('', about, name='about'),
    path('contactus/', contact, name='contactus'),
    path('', tours, name='tours'),
    path('<slug:category_slug>/', tours, name='tours_category'),
    path('<slug:category_slug>/<slug:tour_slug>', tour_detail, name='tour_detail'),
]
