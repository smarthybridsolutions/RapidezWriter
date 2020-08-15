from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import ResumeForm
from .models import Resume

def resume_upload(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resumeAnalysis:uploadresume')
    else:
            form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})


