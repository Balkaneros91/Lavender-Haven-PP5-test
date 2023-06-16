from django.shortcuts import render

# Create your views here.


def items_view(request):
    """ A view to return the items page """

    return render(request, 'items/items.html')
