from django.db import models
from django.contrib.auth.models import User

class StudentInfo(models.Model):
    student_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    date_of_birth = models.DateField()
    academic_year = models.CharField(max_length=20)
    wellness_status = models.CharField(max_length=20)
    password = models.CharField(max_length=9, default='password1234')
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Assignments(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - Due: {self.due_date.strftime('%Y-%m-%d')}"

class Wellness(models.Model):
    WELLNESS_CHOICES = [
        ('Happy', 'Happy 😊'),
        ('Stressed', 'Stressed 😟'),
        ('Tired', 'Tired 😴'),
        ('Motivated', 'Motivated 💪'),
        ('Anxious', 'Anxious 😰'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50, choices=WELLNESS_CHOICES)
    notes = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.mood} "
