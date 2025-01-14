from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class SubService(models.Model):
    service = models.ForeignKey(Service, related_name='subservices', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    condition = models.TextField()
    taux = models.CharField(max_length=100)
    frequence = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class JobInternship(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_job = models.BooleanField(default=True)  # If False, it's an internship
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Credit(models.Model):
    service = models.ForeignKey(Service, related_name='credit', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    condition = models.TextField()
    taux = models.CharField(max_length=100)
    frequence = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='promotion_photos/', blank=True, null=True)

    def __str__(self):
        return self.title


class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    venue = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activity_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    place = models.CharField(max_length=255)
    nationality = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    cv = models.FileField(upload_to='cv_files/')
    cover_letter = models.FileField(upload_to='cover_letter_files/')
    other_documents = models.FileField(upload_to='other_documents/', blank=True, null=True)
    years_of_experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    starting_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Application from {self.full_name}"


# New Testimonial Model
class Testimonial(models.Model):
    name = models.CharField(max_length=255)  # Client's name
    text = models.TextField()  # Testimonial content
    image = models.ImageField(upload_to='testimonial_pictures/', blank=True, null=True)  # Optional profile picture
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of testimonial

    def __str__(self):
        return f"Testimonial by {self.name}"
