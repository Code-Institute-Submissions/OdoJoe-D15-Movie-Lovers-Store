from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Subscriber
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    """
    Index page view
    """
    subscribers = Subscriber.objects.all()
    context = {
        'subscribers': subscribers,
    }
    return render(request, 'home/index.html', context)

def send_newsletter(request):
    """
    return to Newsletter screen once newsletter 
    has been submitted
    """
    
    if request.method == 'POST':
        subject = request.POST['subject']
        content = request.POST['content']
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            send_mail(subject, content, 'newsletter@d15movieloversstore.com', [subscriber.email,], fail_silently=False)
    messages.success(request, f'sent newsletter to {len(subscribers)} users.')
    return render(request, 'home/author.html')

def author_newsletter(request):
    return render(request, 'home/author.html')

def add_to_newsletter(request, user_id):
    """
    View to add subscriber
    """
    user = User.objects.get(id=user_id)

    subscriber = Subscriber()
    subscriber.username = user.username
    subscriber.email = user.email
    subscriber.save()

    return index(request)
