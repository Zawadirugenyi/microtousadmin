from django.contrib import admin
from .models import Service, SubService, JobInternship, Promotion, Activity, TeamMember, Application, Testimonial, Credit

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'condition')
    search_fields = ('name', 'service__name', 'condition')
    list_filter = ('service',)

@admin.register(Credit)  
class CreditAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'condition')
    search_fields = ('name', 'service__name', 'condition')  
    list_filter = ('service',)  

@admin.register(JobInternship)
class JobInternshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_job', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'image')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'start_hour', 'end_hour', 'venue', 'image')
    search_fields = ('name', 'description', 'venue')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'description')
    search_fields = ('name', 'role')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'place', 'nationality', 'sex', 'years_of_experience', 'starting_date')
    search_fields = ('full_name', 'email', 'place', 'nationality')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'text')
