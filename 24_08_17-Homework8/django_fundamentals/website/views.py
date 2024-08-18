from django.shortcuts import render

from meetings.models import Meeting


def welcome(request):
    if request.user.is_authenticated:
        context = {"meetings": Meeting.objects.all()}
    else:
        context = {}
    return render(request, "website/welcome.html", context)
