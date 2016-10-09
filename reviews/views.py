from django.shortcuts import get_object_or_404, render

from .models import Review, Car


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/car_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def car_list(request):
    car_list = Car.objects.order_by('-name')
    context = {'car_list':car_list}
    return render(request, 'reviews/templates/reviews/car_list.html', context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'reviews/car_detail.html', {'car': car})
