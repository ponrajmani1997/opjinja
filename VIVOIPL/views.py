from django.shortcuts import render

# Create your views here.
def CHENNAI(request):
    return render(request,'csk.html',context={'team':'csk','result':'won 2010,2011,2018 trophies'})

def RCB(request):
    return render(request,'rcb.html',context={'team':'rcb','result':'Never won a trophy'})