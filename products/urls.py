from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_stockitems, name='stockitems'),
    path('<stockitem_id>', views.stockitem_detail, name='stockitem_detail'),
]
