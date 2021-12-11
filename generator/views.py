from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/demo.html')

def newhome(request):    
    return HttpResponse('hello there friend !')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
        
    length = int(request.GET.get('length',12))
    thepassword = ''
    
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})

        