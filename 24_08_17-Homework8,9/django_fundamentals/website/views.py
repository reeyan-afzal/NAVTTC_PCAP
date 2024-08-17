from django.shortcuts import render

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html", {"num_meetings": Meeting.objects.count()})
