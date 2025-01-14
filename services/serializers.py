from rest_framework import serializers
from .models import Service, SubService, Credit, JobInternship, Promotion, Activity, TeamMember, Application, Testimonial

# Service Serializer
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description']

# SubService Serializer
class SubServiceSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = SubService
        fields = ['id', 'service', 'name', 'condition', 'taux', 'frequence']

# JobInternship Serializer
class JobInternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobInternship
        fields = ['id', 'title', 'description', 'is_job', 'created_at']

# Promotion Serializer
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'title', 'description', 'created_at', 'image']

# Activity Serializer
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'date', 'start_hour', 'end_hour', 'venue', 'image']

# TeamMember Serializer
class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'role', 'description', 'image']

# Application Serializer
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'full_name', 'email', 'place', 'nationality', 'sex', 'cv', 'cover_letter', 'other_documents', 'years_of_experience', 'starting_date']

# Testimonial Serializer
class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'text', 'image', 'created_at']

# Credit Serializer
class CreditSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()  # Correct field name to 'service'

    class Meta:
        model = Credit
        fields = ['id', 'service', 'name', 'condition', 'taux', 'frequence']  # Correct field names to match the model
