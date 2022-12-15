from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_stockitems, name='stockitems'),
    path('<stockitem_id>', views.stockitem_detail, name='stockitem_detail'),
    path('addreview/', views.add_review, name='add_review'),
    path('deletereview/<review_id>', views.delete_review, name='delete_review'),
    path('showreview/<review_id>', views.show_review, name='show_review'),
    path('editreview/', views.edit_review, name='edit_review'),
]
