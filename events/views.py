from django.shortcuts import render

# Create your views here.


def events_view(request):
    """ A view to return the events page """

    return render(request, 'events/events.html')
