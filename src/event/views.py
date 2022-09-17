

from django.shortcuts import render,redirect
from .models import Event,EventRegister

# Create your views here.

def home(request):
    event = Event.objects.all() 
    for i in event:
        event_id = i.id
        print(event_id)
    context = {
        'event':event,
    }
    return render(request,'home.html',context) 


def view_event(request,id):
    event = Event.objects.get(id=id) 
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        semester = request.POST.get('semester')
        
        
        event_register = EventRegister(
            name = name,
            phone = number,
            email = email,
            current_semester = semester,
            event = event
        )
        
        event_register.save() 
        return redirect('home')

    context = {
        'event':event,
    }
    return render(request,'view_event.html',context) 