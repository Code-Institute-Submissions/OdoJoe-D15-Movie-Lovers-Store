from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Stockitem, Format, Genre


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

    context = {
        'stockitem': stockitem,
    }

    return render(request, 'products/stockitem_detail.html', context)
