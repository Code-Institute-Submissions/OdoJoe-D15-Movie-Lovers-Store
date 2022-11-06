from django.shortcuts import render, get_object_or_404
from .models import Stockitem


def all_stockitems(request):
    """
    show all stock items
    """
    stockitems = Stockitem.objects.all()

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