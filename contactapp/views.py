from django.shortcuts import render
from .forms import contactform

def getContactPage(request):
    contact = contactform()
    return render(request, 'contact.html', {'form': contact})

