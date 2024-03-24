from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializer import EventSerializer
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello people ")

# get all events
@api_view(['GET'])
def getAllEvent(request):
    events = Event.objects.all()
    serializer =EventSerializer(events,many=True)
    return Response(serializer.data)

# get single event
@api_view(['GET'])
def getEvent(request,tag):
    events = Event.objects.get(id=tag)
    serializer =EventSerializer(events)
    return Response(serializer.data)

# add event
@api_view(['POST'])
def addEvent(request):
    serializer =EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update event
@api_view(['PUT'])
def updateEvent(request,tag):
    events = Event.objects.get(id=tag)
    serializer =EventSerializer(instance=events,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete event
@api_view(['DELETE'])
def deleteEvent(request,tag):
    events = Event.objects.get(id=tag)
    events.delete()
    return Response('Item deleted successfully')

