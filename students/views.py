from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from django.contrib.auth.models import User
from .models import StudentProfile


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'students/course_list.html', {'courses': courses})


@login_required
def view_profile(request):
    return render(request, 'students/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.bio = request.POST.get('bio', '')
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        profile.save()
        return redirect('view_profile')
    return render(request, 'students/edit_profile.html', {'profile': profile})