from django.shortcuts import render

# Create your views here.


def contacts_view(request):
    """ A view to return the contacts page """

    return render(request, 'contacts/contacts.html')
