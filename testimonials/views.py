from django.shortcuts import render

# Create your views here.


def testimonials_view(request):
    """ A view to return the testimonials page """

    return render(request, 'testimonials/testimonials.html')
