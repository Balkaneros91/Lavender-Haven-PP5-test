from django.shortcuts import render

# Create your views here.


def subscription_view(request):
    """ A view to return the subscription page """

    return render(request, 'subscription/subscription.html')
