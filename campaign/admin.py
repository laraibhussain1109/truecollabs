from django.contrib import admin
from .models import Campaign, Deliverable

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_pay', 'per_deliverable_pay', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(Deliverable)
class DeliverableAdmin(admin.ModelAdmin):
    list_display = ['campaign', 'influencer', 'deliverable_link', 'is_approved', 'submitted_at']
    list_filter = ['is_approved', 'submitted_at']
    search_fields = ['campaign__title', 'influencer__username']
