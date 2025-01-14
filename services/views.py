from rest_framework import status, viewsets
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Service, SubService, JobInternship, Promotion, 
    Activity, TeamMember, Application, Testimonial, Credit,
)
from .serializers import (
    ServiceSerializer, SubServiceSerializer, JobInternshipSerializer, 
    PromotionSerializer, ActivitySerializer, TeamMemberSerializer, 
    ApplicationSerializer, TestimonialSerializer, CreditSerializer,
)

# Service ViewSet
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# SubService ViewSet
class SubServiceViewSet(viewsets.ModelViewSet):
    queryset = SubService.objects.all()
    serializer_class = SubServiceSerializer

# Testimonial ViewSet
class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

# JobInternship ViewSet
class JobInternshipViewSet(viewsets.ModelViewSet):
    queryset = JobInternship.objects.all()
    serializer_class = JobInternshipSerializer

# Promotion ViewSet
class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

# Activity ViewSet
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# TeamMember ViewSet
class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

# Credit ViewSet
class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        try:
            # Save the application to the database
            application = serializer.save()

            # Send confirmation email to the applicant
            subject_user = 'Application Received - Confirmation'
            message_user = (
                f"Dear {application.full_name},\n\n"
                "Thank you for submitting your application. We have received it and will review it shortly.\n\n"
                "Best regards,\nCoopecMicrotousTeam"
            )
            recipient_list_user = [application.email]

            send_mail(
                subject_user,
                message_user,
                settings.EMAIL_HOST_USER,  # Sender's email
                recipient_list_user,       # Recipient's email (applicant)
                fail_silently=False
            )

            # Send notification email to the admin
            subject_admin = 'New Application Received'
            message_admin = (
                f"A new application has been submitted by {application.full_name}.\n\n"
                f"Details:\nEmail: {application.email}\nPosition Applied: {application.place}\n\n"
                "Please review the application."
            )
            recipient_list_admin = ['coopecmicrotous@gmail.com']  # Replace with your admin email or list of recipients

            send_mail(
                subject_admin,
                message_admin,
                settings.EMAIL_HOST_USER,  # Sender's email
                recipient_list_admin,      # Admin's email
                fail_silently=False
            )

        except Exception as e:
            # Log the error or send a failure notification
            print(f"Error occurred while sending emails: {e}")
            # Optionally, raise an exception to stop the process if needed
            raise
