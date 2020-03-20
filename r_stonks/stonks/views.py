from django.http import HttpResponse
from stonks.models import *


def index(request):

    Portfolio.objects.create(
        title='This got created!',
        date='2020-01-01',
        cash=10000,
        holdings={'AAPL': 4}
        )
    print("This printed!")

    return HttpResponse("Check the terminal")
