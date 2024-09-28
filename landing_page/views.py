from django.shortcuts import render
from .models import MainLandingPage , UserLandingPage , UserRequested
from django.contrib.auth.decorators import login_required
# import messages
from django.contrib import messages
# Create your views here.

def LandingPage(request):
    # get first landing page
    landing_page = MainLandingPage.objects.first()
    context = {
        'landing_page':landing_page
    }
    return render(request,'landing_page.html',context)



@login_required
def UserLandingPagedef(request):
    user = request.user
    user_landing_page = UserLandingPage.objects.filter(user=user).first()
    requested = UserRequested.objects.filter(user=user)
    
    
    context = {
        'user_landing_page':user_landing_page,
        'requested':requested,
    }
    return render(request,'inneruserlandingpage.html',context)


def outuserlandingpage(request,pagename):
    page=UserLandingPage.objects.get(pagename=pagename)
    context={
        'landing_page':page
    }
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        location=request.POST.get('location')
        notes=request.POST.get('notes')or ' '
        #user = CustomUser that create this landing page
        user = page.user
        user_landing_page=UserRequested.objects.create(name=name,email=email,phone=phone,age=age,gender=gender,location=location,notes=notes,user=user)    
        user_landing_page.save()
        messages.success(request, 'your request has been sent successfully')
        return render(request,'userlandingpage.html',context)
    return render(request,'userlandingpage.html',context)


