from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request,'about.html')
def removepunc(request):
    dt = request.GET.get('t', 'default')
    che=request.GET.get('rmpunc','off')
    lc=request.GET.get('lc','off')
    uc=request.GET.get('uc','off')
    rmln=request.GET.get('rmln','off')
    
    punctuations='''!@#$%^&*()_+{}:"?><[];',./'''
    if(che=='on'):
         analysed = "" 
         for char in dt:
             if char not in punctuations:
                 analysed=analysed+char
         params={'purpose':'Removing punctuations','analyse':analysed} 
    elif(lc=='on'): 
         analysed = "" 
         for char in dt:
                 analysed=analysed+char.lower()
         params={'purpose':'Making Lower Case','analyse':analysed}

    elif(uc=='on'): 
         analysed = "" 
         for char in dt:
                 if char!="\n":
                   analysed=analysed+char.upper()
         params={'purpose':'Making Upper Case','analyse':analysed} 
    elif(rmln=='on'): 
         analysed = "" 
         for char in dt:
             if char not in punctuations:
                 analysed=analysed+char.upper()
         params={'purpose':'Removing NewLine','analyse':analysed}         
    else:
         params={'purpose':'NO CHANGES APPLIES TO YOUR TEXT','analyse':analysed}             
    return render(request,'analyse.html',params)

