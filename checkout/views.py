from django.shortcuts import render

# Create your views here.


def checkout_view(request):
    """ A view to return the checkout page """

    return render(request, 'checkout/checkout.html')
