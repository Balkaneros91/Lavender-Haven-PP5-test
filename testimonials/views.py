from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm
from .models import Testimonial

# Create your views here.


def testimonials_view(request):
    """ A view to return the testimonials page """

    return render(request, 'testimonials/testimonials.html')
