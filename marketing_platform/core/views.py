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
