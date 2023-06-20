from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactMessageForm
from .models import Contact, OpenHours


def contacts_view(request):
    """View returning the contacts page"""

    contacts = Contact.objects.first()
    open_hours = OpenHours.objects.all()

    context = {
        'contacts': contacts,
        'open_hours': open_hours,
    }

    return render(request, 'contacts/contacts.html', context)


def contact_message(request):
    """
    Allows user to send a private message to the site admin.
    """
    try:
        if request.method == 'POST':
            redirect_url = request.POST['redirect_url']
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            form = ContactMessageForm(request.POST)
            new_message = form.save(commit=False)
            new_message.name = name
            new_message.email = email
            new_message.message = message
            new_message.save()
            messages.success(request, "Message sent!")
        return redirect(redirect_url)
    except ValueError:
        messages.error(
            request, "Please make sure to fill out your Details \
                before leaving a message.")
        return redirect(redirect_url)


@login_required(login_url='account_login')
def view_message(request, pk):
    """
    Admin can view recieved private messages,
    login & superuser required.
    """
    try:
        if request.user.is_superuser:
            message = get_object_or_404(Message, id=pk)
        else:
            return redirect('home')
    except ValueError:
        messages.error(
            request, "Whoops, looks like you're not authorised to be here!")
    context = {
        'message': message
    }
    return render(request, 'users/message.html', context)


@login_required(login_url='account_login')
def delete_message(request, pk):
    """
    Admin can delete private messages,
    login & superuser required.
    """
    try:
        if request.user.is_superuser:
            message = get_object_or_404(Message, id=pk)
            message.delete()
            return redirect('dashboard')
        else:
            return redirect('home')
    except RuntimeError:
        messages.error(
            request, "Whoops, looks like you're not authorised to be here!")
