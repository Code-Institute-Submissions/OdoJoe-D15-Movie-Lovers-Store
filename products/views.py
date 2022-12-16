from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Stockitem, Format, Genre, Review
from django.core.exceptions import ObjectDoesNotExist


def all_stockitems(request):
    """
    show all stock items
    """
    stockitems = Stockitem.objects.all()
    query = None
    genres = None
    sort = None
    direction = None
    actual_sortkey = None
    user_message = ''
    search_term = None

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            stockitems = stockitems.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)
            search_term = genres[0]

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            actual_sortkey = sortkey
            if sortkey == 'genre':
                sortkey = 'genre__friendly_name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            user_message = f'You are sorting by {actual_sortkey} ({direction}).'
            stockitems = stockitems.order_by(sortkey)

        if 'specialeditions' in request.GET:
            user_message = 'You have selected Special Editions.'
            stockitems = stockitems.filter(is_special_edition=True)

        if 'format' in request.GET:
            uformat = request.GET['format']

            formats = Format.objects.all()
            formats = formats.filter(name=uformat)

            user_message = 'You have selected to view ' + formats[0].friendly_name + '.'
            stockitems = stockitems.filter(format=formats[0].pk)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter search criteria')
                return redirect(reverse('stockitems'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            stockitems = stockitems.filter(queries)
            search_term = query

    current_sorting = f'{actual_sortkey}_{direction}'

    context = {
        'stockitems': stockitems,
        'current_sorting': current_sorting,
        'search_term': search_term,
        'current_genres': genres,
    }

    return render(request, 'products/stockitems.html', context)


def stockitem_detail(request, stockitem_id):
    """
    show one stock item
    """
    stockitem = get_object_or_404(Stockitem, pk=stockitem_id)
    reviews = Review.objects.filter(stockitem=stockitem)
    context = {
        'stockitem': stockitem,
        'reviews': reviews,
    }

    return render(request, 'products/stockitem_detail.html', context)


def add_review(request):
    """
    a view to save reviews
    """
    if request.method == 'POST':
        stockitem_id = request.POST['stockitem_id']
        reviewtext = request.POST['review']
        username = request.POST['username']
        review = Review()
        review.stockitem = get_object_or_404(Stockitem, pk=stockitem_id)
        review.review_text = reviewtext
        review.username = username
        review.save()
        messages.success(request, 'Review Created')

    return stockitem_detail(request, stockitem_id)


def delete_review(request, review_id):
    """
    view to delete review
    """
    try:
        review = Review.objects.get(pk=review_id)
        stockitem_id = review.stockitem.id
        review.delete()
        messages.success(request, 'Review Deleted')
        return stockitem_detail(request, stockitem_id)
    except ObjectDoesNotExist:
        messages.warning(request, 'review does not exist')
        return all_stockitems(request)


def show_review(request, review_id):
    """
    view to show  page to edit reviews
    """
    review = Review.objects.get(pk=review_id)
    context = {
        'review': review,
    }

    return render(request, 'products/edit_review.html', context)


def edit_review(request):
    """
    view to update a review
    """
    if request.method == 'POST':
        review_id = request.POST['review_id']
        new_text = request.POST['review']
        review = Review.objects.get(pk=review_id)
        review.review_text = new_text
        review.save()
        messages.success(request, 'Review Updated')
        return stockitem_detail(request, review.stockitem.id)

    return render(request, 'products/edit_review.html')
