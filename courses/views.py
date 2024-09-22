from django.shortcuts import render, redirect, get_object_or_404
from .models import Course,Feedback
from .forms import CourseForm , CustomUserCreationForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q 

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Set session to expire in 7 days
            request.session.set_expiry(7 * 24 * 60 * 60)  

            if user.is_staff:
                return redirect('course_list')  # Redirect to admin home
            else:
                return redirect('course_list')  # Redirect to client page
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data.get('user_type')
            if user_type == 'admin':
                user.is_staff = True
            else:
                user.is_staff = False
            user.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = CustomUserCreationForm()  # Create a new form instance for GET requests

    return render(request, 'registration/signup.html', {'form': form}) 

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('create_course')  
            else:
                return redirect('client_page')  # Redirect to client page
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login after logout


@login_required
def create_course(request):
    if request.user.studentprofile.role != 'admin':
        return redirect('course_list')  # Redirect students to course list if they're not admin

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('course_detail', course.id)
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})


@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, instructor=request.user)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form, 'course': course})

def course_list(request):

    Courses = Course.objects.all()
    return render(request, 'course_list.html', {'Courses': Courses})


def give_feedback(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(course=course, student=request.user, content=form.cleaned_data['content'])
            return redirect('course_detail', course.id)  # Redirect to course detail after submitting feedback
    else:
        form = FeedbackForm()
    return render(request, 'give_feedback.html', {'course': course, 'form': form})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})
