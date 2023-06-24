from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UpdateNewsletter
from .models import Newsletter


def newsletter(request):
    """
    Allows user to sign up for a newsletter,
    Checks if the email is already in the database,
    Aborts process and informs user if so.
    """
    try:
        if request.method == 'POST':
            email = request.POST['email']
            redirect_url = request.POST['redirect_url']
            already_signed_up = Newsletter.objects.values_list(
                'email', flat=True)

            if email in already_signed_up:
                messages.error(
                    request, "This email address is already signed up!")
            else:
                form = UpdateNewsletter(request.POST)
                newsletter = form.save(commit=False)
                newsletter.email = email
                newsletter.save()
                messages.success(
                    request,
                    f"{email} has been successfully added to our mailing list")
            return redirect(redirect_url)
    except ValueError:
        messages.error(
            request, "Please enter valid Email address....")
        return redirect(redirect_url)


def unsubscribe(request):
    try:
        subscribed = Newsletter.objects.values_list('email', flat=True)

        if request.method == 'POST':
            email = request.POST['email']
            if email in subscribed:
                to_remove = Newsletter.objects.get(email=email)
                to_remove.delete()
                messages.success(
                    request,
                    f"{email} has been removed from our mailing list."
                )
            else:
                messages.error(
                    request,
                    "Sorry we couldn't find that email on our mailing list.")
            return redirect('home')
    except Exception:
        messages.error(
            request, 'Whoops, Houston we have a problem!'
        )
        return redirect('home')
    return render(request, 'subscription/unsubscribe.html')
