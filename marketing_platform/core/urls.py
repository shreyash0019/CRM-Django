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
    reports_view
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
    path('lead-capture/', lead_capture_view, name='lead_capture'),  # Lead Capture Page
    path('contacts/', contacts_view, name='contacts'),  # Contacts Page
    path('reports/', reports_view, name='reports'),  # Reports Page
]
