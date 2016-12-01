from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render, redirect
from django_socketio import broadcast, broadcast_channel, NoSocket

from classgotcha.apps.chat.models import Room
import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
from haikunator import Haikunator



def rooms(request, template="rooms.html"):
    """
    Homepage - lists all rooms.
    """
    context = {"rooms": Room.objects.all()}
    return render(request, template, context)


#def room(request, slug, template="room.html"):
#    """
#    Show a room.
#    """
#    context = {"room": get_object_or_404(Room, slug=slug)}
#    return render(request, template, context)

##############################

def about(request):
    return render(request, "about.html")

def new_room(request):
    """
    Randomly create a new room, and redirect to it.
    """
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = Haikunator.haikunate(Haikunator())
            
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
    return redirect(chat_room, label=label)


def chat_room(request, label):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "room.html", {
        'room': room,
        'messages': messages,
    })

##############################
@user_passes_test(lambda user: user.is_staff)
def system_message(request, template="system_message.html"):
    context = {"rooms": Room.objects.all()}
    if request.method == "POST":
        room = request.POST["room"]
        data = {"action": "system", "message": request.POST["message"]}
        try:
            if room:
                broadcast_channel(data, channel="room-" + room)
            else:
                broadcast(data)
        except NoSocket, e:
            context["message"] = e
        else:
            context["message"] = "Message sent"
    return render(request, template, context)
