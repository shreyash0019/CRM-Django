from django.db import models


class SalesData(models.Model):
    month = models.CharField(max_length=20)
    revenue = models.FloatField()
    
    def __str__(self):
        return f"{self.month}: {self.revenue}"


class LeadCaptureForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class GoogleReview(models.Model):
    user_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class WhatsAppMessage(models.Model):
    recipient = models.CharField(max_length=15)
    message = models.TextField()
    status = models.CharField(max_length=50, choices=[('sent', 'Sent'), ('failed', 'Failed')])
    sent_at = models.DateTimeField(auto_now_add=True)

class EmailCampaign(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipient_list = models.JSONField()
    sent_at = models.DateTimeField(auto_now_add=True)

class SMSCampaign(models.Model):
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

class AIChatbotResponse(models.Model):
    user_query = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ClickToCall(models.Model):
    lead = models.ForeignKey(LeadCaptureForm, on_delete=models.CASCADE)
    call_status = models.CharField(max_length=50)
    recorded_audio = models.FileField(upload_to="call_records/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class SocialMediaPost(models.Model):
    platform = models.CharField(max_length=50, choices=[('facebook', 'Facebook'), ('twitter', 'Twitter')])
    content = models.TextField()
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('scheduled', 'Scheduled'), ('posted', 'Posted')])

class SocialMediaAnalytics(models.Model):
    post = models.ForeignKey(SocialMediaPost, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class LoyaltyProgram(models.Model):
    user_email = models.EmailField()
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class SecurityAudit(models.Model):
    audit_type = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Billing(models.Model):
    client_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=[('paid', 'Paid'), ('pending', 'Pending')])
    created_at = models.DateTimeField(auto_now_add=True)
