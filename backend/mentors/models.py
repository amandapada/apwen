from django.db import models

class Mentor(models.Model):
    DEPARTMENT_CHOICES = [
        ('computer engineering', 'Computer Engineering'),
        ('metallurgical engineering', 'Metallurgical Engineering'),
        ('electrical engineering', 'Electrical Engineering'),
        ('telecommunication engineering', 'Telecommunication Engineering'),
        ('civil engineering', 'Civil Engineering'),
        ('mechanical engineering', 'Mechanical Engineering'),
        ('polymer and textile engineering', 'Polymer and Textile Engineering'),
        ('agricultural engineering', 'Agricultural Engineering'),
        ('chemical engineering', 'Chemical Engineering'),
        ('water resources and environmental engineering', 'Water Resources and Environmental Engineering'),
    ]

    LEVEL_CHOICES = [
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    number_of_mentees = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.department})"

class Mentee(models.Model):
    LEVEL_CHOICES = [
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
    ]

    DEPARTMENT_CHOICES = [
        ('computer engineering', 'Computer Engineering'),
        ('metallurgical engineering', 'Metallurgical Engineering'),
        ('electrical engineering', 'Electrical Engineering'),
        ('telecommunication engineering', 'Telecommunication Engineering'),
        ('civil engineering', 'Civil Engineering'),
        ('mechanical engineering', 'Mechanical Engineering'),
        ('polymer and textile engineering', 'Polymer and Textile Engineering'),
        ('agricultural engineering', 'Agricultural Engineering'),
        ('chemical engineering', 'Chemical Engineering'),
        ('water resources and environmental engineering', 'Water Resources and Environmental Engineering'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    mentor_department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.level})'
