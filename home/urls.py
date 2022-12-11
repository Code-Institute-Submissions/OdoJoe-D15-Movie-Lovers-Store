from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newsletter/<user_id>', views.add_to_newsletter, name='add_to_newsletter'),
    path('newsletter/', views.author_newsletter, name='author_newsletter'),
    path('send/', views.send_newsletter, name='send_newsletter'),
]

handler404 = 'home.views.handler404'

