from django.shortcuts import render, redirect, get_object_or_404
from .models import Newsletter
from .forms import NewsletterForm

# Create your views here.


def subscription_view(request):
    """ A view to return the subscription page """

    return render(request, 'subscription/subscription.html')


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter:success')
    else:
        form = NewsletterForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})


def unsubscribe(request, subscriber_id):
    subscriber = get_object_or_404(Newsletter, pk=subscriber_id)
    if request.method == 'POST':
        subscriber.is_subscribed = False
        subscriber.save()
        return redirect('newsletter:unsubscribe_success')
    return render(request, 'newsletter/unsubscribe.html', {'subscriber': subscriber})


def success(request):
    return render(request, 'newsletter/success.html')


def unsubscribe_success(request):
    return render(request, 'newsletter/unsubscribe_success.html')
