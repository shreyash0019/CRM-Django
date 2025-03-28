from django.contrib import admin
from .models import (
    LeadCaptureForm, GoogleReview, WhatsAppMessage, EmailCampaign, SMSCampaign,
    AIChatbotResponse, ClickToCall, SocialMediaPost, SocialMediaAnalytics,
    LoyaltyProgram, SecurityAudit, Billing
)

@admin.register(LeadCaptureForm)
class LeadCaptureFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(GoogleReview)
class GoogleReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'rating', 'created_at')
    search_fields = ('user_name',)
    list_filter = ('rating', 'created_at')

@admin.register(WhatsAppMessage)
class WhatsAppMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'message', 'status', 'sent_at')
    list_filter = ('status', 'sent_at')

@admin.register(EmailCampaign)
class EmailCampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'sent_at')
    search_fields = ('subject',)
    list_filter = ('sent_at',)

@admin.register(SMSCampaign)
class SMSCampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'message', 'sent_at')
    search_fields = ('phone_number',)
    list_filter = ('sent_at',)

@admin.register(AIChatbotResponse)
class AIChatbotResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_query', 'bot_response', 'created_at')
    search_fields = ('user_query',)
    list_filter = ('created_at',)

@admin.register(ClickToCall)
class ClickToCallAdmin(admin.ModelAdmin):
    list_display = ('id', 'lead', 'call_status', 'created_at')
    list_filter = ('call_status', 'created_at')

@admin.register(SocialMediaPost)
class SocialMediaPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'platform', 'content', 'scheduled_time', 'status')
    search_fields = ('platform',)
    list_filter = ('status', 'scheduled_time')

@admin.register(SocialMediaAnalytics)
class SocialMediaAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'likes', 'comments', 'shares', 'created_at')
    list_filter = ('created_at',)

@admin.register(LoyaltyProgram)
class LoyaltyProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_email', 'points', 'created_at')
    search_fields = ('user_email',)
    list_filter = ('created_at',)

@admin.register(SecurityAudit)
class SecurityAuditAdmin(admin.ModelAdmin):
    list_display = ('id', 'audit_type', 'status', 'created_at')
    list_filter = ('status', 'created_at')

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'amount', 'invoice_number', 'status', 'created_at')
    search_fields = ('client_name', 'invoice_number')
    list_filter = ('status', 'created_at')
