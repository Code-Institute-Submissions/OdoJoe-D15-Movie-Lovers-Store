from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Stockitem


def bag_contents(request):

    bag_items = []
    total = 0
    stockitem_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        stockitem = get_object_or_404(Stockitem, pk=item_id)
        total += quantity * stockitem.price
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'stockitem': stockitem,
        })

    if total > 0:
        delivery = Decimal(settings.STANDARD_DELIVERY_FEE)
    else:
        delivery = 0
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'stockitem_count': stockitem_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
