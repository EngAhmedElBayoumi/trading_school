from django.shortcuts import render
from .models import MainLandingPage , UserLandingPage , UserRequested 
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
# import messages
from django.contrib import messages
# Create your views here.

def LandingPage(request):
    # get first landing page
    landing_page = MainLandingPage.objects.first()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        location=request.POST.get('location')
        notes=request.POST.get('notes')or ' '
        
        user_landing_page=UserRequested.objects.create(name=name,email=email,phone=phone,age=age,gender=gender,location=location,notes=notes)    
        user_landing_page.save()
        messages.success(request, 'your request has been sent successfully')
    
    
    
    
    context = {
        'landing_page':landing_page
    }
    return render(request,'landing_page.html',context)

@login_required
def UserLandingPagedef(request):
    user = request.user
    user_landing_page = UserLandingPage.objects.filter(user=user).first()
    requested = UserRequested.objects.filter(user=user)
    
    if request.method=='POST':
        image=request.FILES.get('image')
        video=request.FILES.get('video')
        title=request.POST.get('title')
        title_ar=request.POST.get('title_ar')
        description=request.POST.get('description')
        description_ar=request.POST.get('description_ar')
        
        # get name for user from his profile 
        user_profile = Profile.objects.get(user=user)
        print("pagename=" , user_profile.name)
        
        if user_landing_page:
            user_landing_page.image=image
            user_landing_page.video=video
            user_landing_page.title=title
            user_landing_page.title_ar=title_ar
            user_landing_page.description=description
            user_landing_page.description_ar=description_ar
            user_landing_page.pagename=user_profile.name
            user_landing_page.save()
            messages.success(request, 'your profile has been updated successfully')
        else:
            user_landing_page = UserLandingPage.objects.create(user=user)
            user_landing_page.image=image
            user_landing_page.video=video
            user_landing_page.title=title
            user_landing_page.title_ar=title_ar
            user_landing_page.description=description
            user_landing_page.description_ar=description_ar
            user_landing_page.pagename=user_profile.name
            user_landing_page.save()
            messages.success(request, 'your profile has been created successfully')
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




#-------------------------ar --------------------------


def LandingPage_ar(request):
    # get first landing page
    landing_page = MainLandingPage.objects.first()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        location=request.POST.get('location')
        notes=request.POST.get('notes')or ' '
        user_landing_page=UserRequested.objects.create(name=name,email=email,phone=phone,age=age,gender=gender,location=location,notes=notes)    
        user_landing_page.save()
        messages.success(request, 'your request has been sent successfully')
    
    context = {
        'landing_page':landing_page
    }
    return render(request,'ar/landing_page.html',context)

@login_required
def UserLandingPagedef_ar(request):
    user = request.user
    user_landing_page = UserLandingPage.objects.filter(user=user).first()
    requested = UserRequested.objects.filter(user=user)
    
    if request.method=='POST':
        image=request.FILES.get('image')
        video=request.FILES.get('video')
        title=request.POST.get('title')
        title_ar=request.POST.get('title_ar')
        description=request.POST.get('description')
        description_ar=request.POST.get('description_ar')
        
        # get name for user from his profile 
        user_profile = Profile.objects.get(user=user)
        print("pagename=" , user_profile.name)
        
        if user_landing_page:
            user_landing_page.image=image
            user_landing_page.video=video
            user_landing_page.title=title
            user_landing_page.title_ar=title_ar
            user_landing_page.description=description
            user_landing_page.description_ar=description_ar
            user_landing_page.pagename=user_profile.name
            user_landing_page.save()
            messages.success(request, 'your profile has been updated successfully')
        else:
            user_landing_page = UserLandingPage.objects.create(user=user)
            user_landing_page.image=image
            user_landing_page.video=video
            user_landing_page.title=title
            user_landing_page.title_ar=title_ar
            user_landing_page.description=description
            user_landing_page.description_ar=description_ar
            user_landing_page.pagename=user_profile.name
            user_landing_page.save()
            messages.success(request, 'your profile has been created successfully')
    context = {
        'user_landing_page':user_landing_page,
        'requested':requested,
    }
    return render(request,'ar/inneruserlandingpage.html',context)


def outuserlandingpage_ar(request,pagename):
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
        return render(request,'ar/userlandingpage.html',context)
    return render(request,'ar/userlandingpage.html',context)





