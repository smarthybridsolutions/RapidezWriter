from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact_us(request):
    return render(request,"contact.html")

def resume_consulting(request):
    return render(request,"resume_consulting.html")

def resume_writing(request):
    return render(request,"resume_writing.html")

def resume_makeover(request):
    return render(request,"resume_makeover.html")
def resume_makeover_1(request):
    return render(request,"resume_makeover1.html")
def resume_makeover_2(request):
    return render(request,"resume_makeover2.html")

def resume_video(request):
    return render(request,"resume_video.html")

def linkedin(request):
    return render(request,"linkedin.html")

def testimonials(request):
    return render(request,"testimonials.html")