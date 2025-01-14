from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Initialize DefaultRouter and register viewsets
router = DefaultRouter()
router.register(r'services', views.ServiceViewSet)
router.register(r'subservices', views.SubServiceViewSet)
router.register(r'jobinternships', views.JobInternshipViewSet)
router.register(r'promotions', views.PromotionViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'team_members', views.TeamMemberViewSet)
router.register(r'applications', views.ApplicationViewSet)
router.register(r'credit', views.CreditViewSet)
router.register(r'testimonials', views.TestimonialViewSet)  # Add TestimonialViewSet

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]

# Serve media files during development if DEBUG is True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
