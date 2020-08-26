"""rapidezWriter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# for Media files URLS
from django.conf import settings
from django.conf.urls.static import static
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('About', views.about, name="about"),
    path('Contact-Us', views.contact_us, name="contactUs"),
    path('Resume-Consulting', views.resume_consulting, name="resumeConsulting"),
    path('Resume-Writing', views.resume_writing, name="resumeWriting"),
    path('Resume-Makeover', views.resume_makeover, name="resumeMakeover"),
    path('Resume-Makeover1', views.resume_makeover_1, name="resumeMakeover1"),
    path('Resume-Makeover2', views.resume_makeover_2, name="resumeMakeover2"),
    path('Resume-Video', views.resume_video, name="resumeVideo"),

    path('linkedIn', views.linkedin, name="linkedIn"),

    path('Testimonials', views.testimonials, name="testimonials")

]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
