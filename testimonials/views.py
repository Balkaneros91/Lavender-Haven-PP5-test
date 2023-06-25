from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

from .forms import ReviewForm
from .models import Review

import uuid

# Create your views here.


# def testimonials_view(request):
#     """ A view to return the testimonials page """

#     return render(request, 'testimonials/testimonials.html')


# def reviews_list(request):
#     reviews = Review.objects.all()
#     for review in reviews:
#         review.uuid = uuid.uuid4()  # Set the UUID value for each review
#     context = {'reviews': reviews}
#     return render(request, 'testimonials/review_list.html', context)


@login_required
def reviews_list(request):

    if request.user.is_superuser:
        reviews = Review.objects.all()
        for review in reviews:
            review.uuid = uuid.uuid4()  # Set the UUID value for each review
    else:
        reviews = Review.objects.filter(user=request.user)

    context = {'reviews': reviews}
    return render(request, 'testimonials/testimonials_list.html', context)


@login_required(login_url='account_login')
def add_review(request):
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Your review awaits for approval.')
            return redirect('testimonials:review_list')

    context = {'form': review_form}
    return render(request, 'testimonials/add_testimonial.html', context)


# def booking_confirmation(request):
#     review = Review.objects.first()
#     context = {'Review': Review}
#     return render(request,
#                   'testimonials/review_confirmation.html', context)


@login_required(login_url='account_login')
def edit_review(request, id):
    review = get_object_or_404(Review, id=id)

    # Check if the logged-in user is the owner of the booking
    if review.user != request.user:
        return HttpResponseForbidden("You don't have permission to access this review.")

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review successfully updated!')
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)
    context = {'form': form}
    return render(request, 'testimonials/edit_testimonial.html', context)


# @login_required
# def delete_review(request, pk):
#     review = get_object_or_404(Booking, pk=pk)

#     if request.method == 'POST':
#         review.delete()
#         messages.success(request, 'Review successfully deleted!')
#         return redirect('review_list')
#     context = {'review': review}
#     return render(request, 'testimonials/delete_testimonial.html', context)









# @login_required(login_url='account_login')
# def leave_review(request):
#     """
#     User can submit a product review,
#     They must be logged in to do so.
#     """
#     form = ReviewForm()
#     try:
#         if request.method == 'POST':
#             form = ReviewForm(request.POST)
#             if form.is_valid():
#                 update = form.save(commit=False)
#                 update.email = request.user.email
#                 update.save()
#                 messages.success(
#                     request, "Review saved, Thank you for your feedback.")
#                 return redirect('home')
#             else:
#                 messages.error(request, "Please fill in the form...")
#     except ValueError:
#         messages.error(
#             request,
#             "Whoops! something has gone wrong, we'll get right on to it.")
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/leave_review.html', context)


# @login_required(login_url='account_login')
# def view_review(request, pk):
#     """
#     Admin can see and update visibility of customer reviews.
#     """
#     review = get_object_or_404(Review, id=pk)
#     form = ReviewForm(instance=review)
#     try:
#         if request.method == 'POST' and request.user.is_superuser:
#             form = ReviewForm(request.POST, instance=review)
#             if form.is_valid():
#                 form.save()
#                 messages.success(
#                     request, "Review saved.")
#                 return redirect('dashboard')
#             else:
#                 messages.error(request, "Please fill in the form...")
#     except ValueError:
#         messages.error(
#             request,
#             "Whoops! something has gone wrong, we'll get right on to it.")
#     context = {
#         'review': review,
#         'form': form
#     }
#     return render(request, 'users/review.html', context)


# @login_required(login_url='account_login')
# def delete_review(request, pk):
#     """
#     Admin can delete customer reviews,
#     Required to be logged in and a superuser.
#     """
#     try:
#         if request.user.is_superuser:
#             review = get_object_or_404(Review, id=pk)
#             review.delete()
#             return redirect('dashboard')
#     except RuntimeError:
#         messages.error(
#             request, "Whoops, looks like you're not authorised to be here!")
