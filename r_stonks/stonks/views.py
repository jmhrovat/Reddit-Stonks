from django.http import HttpResponse


def index(request):

    print("This printed!")

    return HttpResponse("Check the terminal")
