from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Stockitem, Format


def all_stockitems(request):
    """
    show all stock items
    """
    stockitems = Stockitem.objects.all()
    query = None
    user_message = ''

    if request.GET:
        if 'specialeditions' in request.GET:
            user_message = 'You have selected Special Editions.'
            stockitems = stockitems.filter(is_special_edition=True)
            messages.add_message(request, messages.INFO, user_message)
        if 'format' in request.GET:
            
            uformat = request.GET['format']

            formats = Format.objects.all()
            formats = formats.filter(name=uformat)

            user_message = 'You have selected to view ' + formats[0].friendly_name + '.'
            messages.add_message(request, messages.INFO, user_message)
            stockitems = stockitems.filter(format=formats[0].pk)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter search criteria')
                return redirect(reverse('stockitems'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            stockitems = stockitems.filter(queries)

    context = {
        'stockitems': stockitems,
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