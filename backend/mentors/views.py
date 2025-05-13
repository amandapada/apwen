from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mentor, Mentee

def add_mentor_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        other_name = request.POST.get('other-name')
        department = request.POST.get('departments')
        level = request.POST.get('mentor-level')
        phone_number = request.POST.get('phone-number')
        email = request.POST.get('email')
        number_of_mentees = request.POST.get('number-of-mentees')

        if not all([first_name, last_name, department, level, phone_number, email, number_of_mentees]):
            messages.error(request, "Please fill in all required fields.")
            return redirect('add-mentor')

        Mentor.objects.create(
            first_name=first_name,
            last_name=last_name,
            other_name=other_name,
            department=department,
            level=level,
            phone_number=phone_number,
            email=email,
            number_of_mentees=number_of_mentees,
        )
        messages.success(request, "Mentor added successfully.")
        return redirect('add-mentor')

    return render(request, 'mentor_form.html')


def add_mentee_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        other_name = request.POST.get('other-name')
        department = request.POST.get('departments')
        mentor_department = request.POST.get('mentor-department') or request.POST.get('departments')  # fallback
        level = request.POST.get('mentor-level')
        phone_number = request.POST.get('phone-number')
        email = request.POST.get('email')

        if Mentee.objects.filter(email=email).exists():
            messages.error(request, 'Mentee with this email already exists.')
            return redirect('register-mentee')

        mentee = Mentee.objects.create(
            first_name=first_name,
            last_name=last_name,
            other_name=other_name,
            department=department,
            mentor_department=mentor_department,
            level=level,
            phone_number=phone_number,
            email=email,
        )
        messages.success(request, 'Mentee registered successfully.')
        return redirect('register-mentee')

    return render(request, 'register_mentee.html') 