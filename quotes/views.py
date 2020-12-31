from django.shortcuts import render

from quotes.models import Quote


def home_view(request):
    quotes = Quote.objects.all()
    context = {
        'quotes': quotes
    }
    return render(request, 'home.html', context)
