from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Subscriber

def index(request):
    """
    Index page view
    """
    return render(request, 'home/index.html')


def add_to_newsletter(request, user_id):
    """
    View to add subscriber
    """
    user = User.objects.get(id=user_id)

    subscriber = Subscriber()
    subscriber.username = user.username
    subscriber.email = user.email
    subscriber.save()

    subscribers = Subscriber.objects.all()
    context = {
        'subscribers': subscribers,
    }
    return render(request, 'home/index.html', context)
