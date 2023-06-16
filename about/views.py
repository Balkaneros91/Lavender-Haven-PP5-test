from django.shortcuts import render

# Create your views here.


def about_view(request):
    """ A view to return the about page """

    return render(request, 'about/about.html')
