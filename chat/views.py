from django.shortcuts import render

from chat.models import ChatMessages

# Create your views here.
# def index(request):
#     return render(request, 'chat/index.html')

def index(request):
    # groups=ChatMessages.objects.all()
    res = set(ChatMessages.objects.values_list('text_name', flat=True))
    print(res)
    context= {"group":res}
    return render(request, 'chat/index.html', context)

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })