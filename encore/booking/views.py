from django.shortcuts import render


def book(request):
    return render(request, "booking/bookPage.html")