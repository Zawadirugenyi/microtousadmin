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

# -------------------------------
# Basic ModelViewSets
# -------------------------------
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SubServiceViewSet(viewsets.ModelViewSet):
    queryset = SubService.objects.all()
    serializer_class = SubServiceSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class JobInternshipViewSet(viewsets.ModelViewSet):
    queryset = JobInternship.objects.all()
    serializer_class = JobInternshipSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer

# -------------------------------
# Application ViewSet
# -------------------------------
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        """
        Override create to:
        1. Save application first
        2. Send emails safely
        3. Always return serialized data
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save()  # ✅ save first

        # Send emails safely
        try:
            self.send_emails(application)
        except Exception as e:
            print(f"Email sending failed: {e}")
            # Do not raise exception → frontend still gets response

        # Return the created application data
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def send_emails(self, application):
        """
        Send confirmation to user and notification to admin.
        Separated into a method to keep create() clean.
        """
        # Send confirmation email to user
        subject_user = 'Application Received - Confirmation'
        message_user = (
            f"Dear {application.full_name},\n\n"
            "Thank you for submitting your application. We have received it "
            "and will review it shortly.\n\n"
            "Best regards,\nCoopecMicrotousTeam"
        )
        send_mail(
            subject_user,
            message_user,
            settings.EMAIL_HOST_USER,
            [application.email],
            fail_silently=False
        )

        # Send notification email to admin
        subject_admin = 'New Application Received'
        message_admin = (
            f"A new application has been submitted by {application.full_name}.\n\n"
            f"Details:\nEmail: {application.email}\nPosition Applied: {application.place}\n\n"
            "Please review the application."
        )
        send_mail(
            subject_admin,
            message_admin,
            settings.EMAIL_HOST_USER,
            ['coopecmicrotous@gmail.com'],
            fail_silently=False
        )