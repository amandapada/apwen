from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email_or_phone, password=None, **extra_fields):
        if not email_or_phone:
            raise ValueError("Email or phone is required")
        user = self.model(email_or_phone=email_or_phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_or_phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', User.Role.ADMIN)
        return self.create_user(email_or_phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'
        MENTOR = 'mentor', 'Mentor'

    email_or_phone = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email_or_phone'

    def __str__(self):
        return self.email_or_phone


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    othername = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class MentorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor_profile')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    othername = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    number_of_mentees = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Mentorship(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    mentor = models.ForeignKey(MentorProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} -> {self.mentor}"


class MentorRequest(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request by {self.student}"
