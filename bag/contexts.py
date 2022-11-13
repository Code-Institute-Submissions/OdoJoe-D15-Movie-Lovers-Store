from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    stockitem_count = 0

    if total >0:
        delivery = total + Decimal(settings.STANDARD_DELIVERY_FEE)
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
