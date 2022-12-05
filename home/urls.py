from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<user_id>', views.add_to_newsletter, name='add_to_newsletter'),
]
