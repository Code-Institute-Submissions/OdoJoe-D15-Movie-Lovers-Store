from django.shortcuts import render
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
