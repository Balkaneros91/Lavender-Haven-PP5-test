from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactMessageForm
from .models import Contact, OpenHours, ContactMessage


# def contacts_view(request):
#     """
#     View returning the contacts page and handling contact message submission.
#     """
#     contacts = Contact.objects.first()
#     open_hours = OpenHours.objects.all()

#     try:
#         if request.method == 'POST':
#             redirect_url = request.POST['redirect_url']
#             name = request.POST['name']
#             email = request.POST['email']
#             message = request.POST['message']
#             form = ContactMessageForm(request.POST)
#             new_message = form.save(commit=False)
#             new_message.name = name
#             new_message.email = email
#             new_message.message = message
#             new_message.save()
#             messages.success(request, "Message sent!")
#         return redirect(redirect_url)
#     except ValueError:
#         messages.error(
#             request, "Please make sure to fill out your Details \
#                 before leaving a message.")
#         return redirect(redirect_url)

#     context = {
#         'contacts': contacts,
#         'open_hours': open_hours,
#         'contact_form': ContactMessageForm()  # Create a new form instance to render in the template
#     }

#     return render(request, 'contacts/contacts.html', context)


def contacts_view(request):
    """
    View returning the contacts page and handling contact message submission.
    """
    if request.method == 'POST':
        redirect_url = request.POST.get('redirect_url', '/')
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent!")
        else:
            messages.error(
                request, "Please make sure to fill out all the fields.")
        return redirect(redirect_url)

    contacts = Contact.objects.first()
    open_hours = OpenHours.objects.all()

    context = {
        'contacts': contacts,
        'open_hours': open_hours,
        # Create a new form instance to render in the template
        'contact_form': ContactMessageForm()
    }

    return render(request, 'contacts/contacts.html', context)

# def contacts_view(request):
#     """View returning the contacts page"""
#     contacts = Contact.objects.first()
#     open_hours = OpenHours.objects.all()
#     context = {
#         'contacts': contacts,
#         'open_hours': open_hours,
#     }
#     return render(request, 'contacts/contacts.html', context)


# def contact_message(request):
#     """
#     Allows user to send a private message to the site admin.
#     """
#     try:
#         if request.method == 'POST':
#             redirect_url = request.POST['redirect_url']
#             name = request.POST['name']
#             email = request.POST['email']
#             message = request.POST['message']
#             form = ContactMessageForm(request.POST)
#             new_message = form.save(commit=False)
#             new_message.name = name
#             new_message.email = email
#             new_message.message = message
#             new_message.save()
#             messages.success(request, "Message sent!")
#         return redirect(redirect_url)
#     except ValueError:
#         messages.error(
#             request, "Please make sure to fill out your Details \
#                 before leaving a message.")
#         return redirect(redirect_url)


# def contact(request):
#     """ Contact Form """
#     form = ContactForm
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry"
#             body = {
#                     'name': form.cleaned_data['name'],
#                     'email': form.cleaned_data['email'],
#                     'message_subject': form.cleaned_data['message_subject'],
#                     'message': form.cleaned_data['message'],
#             }
#             contact = form.save()
#             messages.success(request, f'Query sent')
#             return redirect(reverse('home'))
#         else:
#             form = ContactForm()

#     return render(request, "contacts/contacts.html", {'form': form})
