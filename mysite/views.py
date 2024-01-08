from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request,'about.html')
def removepunc(request):
    dt = request.POST.get('t', 'default')
    che=request.POST.get('rmpunc','off')
    lc=request.POST.get('lc','off')
    uc=request.POST.get('uc','off')
    rmln=request.POST.get('rmln','off')
    
    punctuations='''!@#$%^&*()_+{}:"?><[];',./'''
    if(che=='on'):
         analysed = "" 
         for char in dt:
             if char not in punctuations:
                 analysed=analysed+char
         params={'purpose':'Removing punctuations','analyse':analysed} 
         dt=analysed
    if(lc=='on'): 
         analysed = "" 
         for char in dt:
                 analysed=analysed+char.lower()
         params={'purpose':'Making Lower Case','analyse':analysed}
         dt=analysed
    if(uc=='on'): 
         analysed = "" 
         for char in dt:
                 if char!="\n":
                   analysed=analysed+char.upper()
         params={'purpose':'Making Upper Case','analyse':analysed} 
         dt=analysed
    if(rmln=='on'): 
         analysed = "" 
         for char in dt:
             if char not in punctuations:
                 analysed=analysed+char.upper()
         params={'purpose':'Removing NewLine','analyse':analysed}     
         dt=analysed    
       
    params={'purpose':'Removing NewLine','analyse':analysed}              
    return render(request,'analyse.html',params)

