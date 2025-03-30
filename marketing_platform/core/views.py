from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import LeadCaptureForm
from .serializers import LeadCaptureFormSerializer

# JWT Token Views
class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom JWT Login View"""
    pass

class CustomTokenRefreshView(TokenRefreshView):
    """Refresh JWT Token"""
    pass

# Lead Capture Form API (Protected)
class LeadCaptureFormViewSet(viewsets.ModelViewSet):
    """
    API to Create, Retrieve, Update, and Delete Lead Capture Forms.
    JWT authentication required.
    """
    queryset = LeadCaptureForm.objects.all()
    serializer_class = LeadCaptureFormSerializer
    permission_classes = [IsAuthenticated]  # Protect API with JWT Authentication

    def create(self, request, *args, **kwargs):
        """Create a new Lead Capture Form"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        """Retrieve all Lead Capture Forms"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a single Lead Capture Form by ID"""
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update an existing Lead Capture Form"""
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete a Lead Capture Form"""
        return super().destroy(request, *args, **kwargs)

# UI Views (Render HTML Pages)
def home_view(request):
    """Render the Home Page"""
    return render(request, 'core/home.html')

def login_view(request):
    """Render the Login Page"""
    return render(request, 'core/login.html')

def dashboard_view(request):
    """Render the Dashboard Page"""
    return render(request, 'core/dashboard.html')

def lead_capture_view(request):
    """Render the Lead Capture Form Page"""
    return render(request, 'core/lead_capture.html')

def contacts_view(request):
    """Render the Contacts Page"""
    return render(request, 'core/contacts.html')

def reports_view(request):
    """Render the Reports Page"""
    return render(request, 'core/reports.html')

# Protected API Example
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    """
    Example protected view that requires authentication.
    """
    return Response({"message": "You have access to this protected route!", "user": str(request.user)})

# UI Views (Render HTML Pages)
def google_reviews_view(request):
    """Render the Google Reviews Page"""
    return render(request, 'core/google_reviews.html')

def whatsapp_marketing_view(request):
    """Render the WhatsApp Marketing Page"""
    return render(request, 'core/whatsapp_marketing.html')

def email_sms_marketing_view(request):
    """Render the Email & SMS Marketing Page"""
    return render(request, 'core/email_sms_marketing.html')

def ai_chatbot_view(request):
    """Render the AI Chatbot Page"""
    return render(request, 'core/ai_chatbot.html')

def click_to_call_view(request):
    """Render the Click-to-Call Page"""
    return render(request, 'core/click_to_call.html')

def social_media_view(request):
    """Render the Social Media Scheduler Page"""
    return render(request, 'core/social_media.html')

def loyalty_referral_view(request):
    """Render the Loyalty & Referral Programs Page"""
    return render(request, 'core/loyalty_referral.html')

def security_services_view(request):
    """Render the Security Services Page"""
    return render(request, 'core/security_services.html')

def client_billing_view(request):
    """Render the Client Billing System Page"""
    return render(request, 'core/client_billing.html')

from django.shortcuts import render
from .models import SalesData
from django.http import JsonResponse

def dashboard(request):
    return render(request, 'dashboard.html')

def sales_data(request):
    sales = SalesData.objects.all().order_by('id')
    data = {
        "labels": [sale.month for sale in sales],
        "data": [sale.revenue for sale in sales]
    }
    return JsonResponse(data)
