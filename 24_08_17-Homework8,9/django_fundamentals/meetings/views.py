from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from meetings.models import Meeting, Room

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')  # Adjust this to your preferred redirection
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


@login_required
def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[])


@login_required
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm

    return render(request, "meetings/new.html", {"form": form})


@login_required
def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
    else:
        form = MeetingForm(instance=meeting)

    return render(request, "meetings/edit.html", {"form": form})


@login_required
def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("welcome")
    else:
        return render(request, "meetings/confirm_delete.html", {"meeting": meeting})
