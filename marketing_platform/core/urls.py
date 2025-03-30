from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    LeadCaptureFormViewSet,
    protected_view,
    home_view,
    login_view,
    dashboard_view,
    lead_capture_view,
    contacts_view,
    reports_view,
    google_reviews_view,
    whatsapp_marketing_view,
    email_sms_marketing_view,
    ai_chatbot_view,
    click_to_call_view,
    social_media_view,
    loyalty_referral_view,
    security_services_view,
    client_billing_view,
    sales_data
)

# Router for API ViewSet
router = DefaultRouter()
router.register(r'lead-capture', LeadCaptureFormViewSet, basename='lead-capture')

urlpatterns = [
    # ------------------- API Endpoints -------------------

    # JWT Authentication URLs
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    # Protected API Example
    path('api/protected/', protected_view, name='protected'),

    # Lead Capture API
    path('api/', include(router.urls)),

    # ------------------- UI Endpoints -------------------

    path('', home_view, name='home'),                # Home Page
    path('login/', login_view, name='login'),        # Login Page
    path('dashboard/', dashboard_view, name='dashboard'),  # Dashboard
    path('sales-data/', sales_data, name='sales_data'),
    path('lead-capture/', lead_capture_view, name='lead_capture'),  # Lead Capture Page
    path('contacts/', contacts_view, name='contacts'),  # Contacts Page
    path('reports/', reports_view, name='reports'),  # Reports Page
    path('google-reviews/', google_reviews_view, name='google_reviews'),  # Google Reviews Page
    path('whatsapp-marketing/', whatsapp_marketing_view, name='whatsapp_marketing'),  # WhatsApp Marketing Page
    path('email-sms-marketing/', email_sms_marketing_view, name='email_sms_marketing'),  # Email & SMS Marketing Page
    path('ai-chatbot/', ai_chatbot_view, name='ai_chatbot'),  # AI Chatbot Page
    path('click-to-call/', click_to_call_view, name='click_to_call'),  # Click-to-Call Feature
    path('social-media/', social_media_view, name='social_media'),  # Social Media Scheduler
    path('loyalty-referral/', loyalty_referral_view, name='loyalty_referral'),  # Loyalty & Referral Programs
    path('security-services/', security_services_view, name='security_services'),  # Security Services
    path('client-billing/', client_billing_view, name='client_billing'),  # Client Billing System
]
