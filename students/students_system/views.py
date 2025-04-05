from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib import messages  # If using messages for success
from .models import User, Assignments,Wellness  
from . import forms
from .forms import AssignmentForm  # Ensure this matches your form name

from .forms import UserRegistrationForm, AssignmentForm  # Ensure these forms are correctly defined

# View for handling the register functionality
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect("success_message")
    else:
        form = UserRegistrationForm()
    
    return render(request, "students_system/register.html", {"form": form})

# Login view
def login(request):
    return render(request, 'students_system/login.html')

# Success message view after registration
def success_message(request):
    return render(request, 'students_system/success_message.html')

# Dashboard view with data about users and active projects
def dashboard(request):
    total_users = User.objects.count()  # Correct model name
    active_projects = Assignment.objects.filter(completed=False).count()  # Correct model name
    notifications = ["New course available", "Exam schedule updated", "Profile verification needed"]
    recent_activities = ["You updated your profile", "New message received", "Project deadline is approaching"]

    context = {
        'total_users': total_users,
        'active_projects': active_projects,
        'notifications': notifications,
        'recent_activities': recent_activities,
    }
    return render(request, 'students_system/dashboard.html', context)

# Logout functionality
def logout(request):
    django_logout(request)
    return redirect('students_system/login')

# Assignments page view
#def assignments(request):
   # form = forms.AssignmentForm()  # Make sure 'AssignmentForm' exists in forms.py
    #return render(request, 'assignments.html', {'form': form})

def assignments(request):
 all_assignments = Assignments.objects.all()
 return render(request, 'students_system/assignments.html', {'assignments': all_assignments})

# Wellness page view
def wellness(request):
    return render(request, 'students_system/wellness.html')
