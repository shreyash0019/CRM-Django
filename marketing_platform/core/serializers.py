from rest_framework import serializers
from .models import *

class LeadCaptureFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadCaptureForm
        fields = '__all__'

class GoogleReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleReview
        fields = '__all__'

# Repeat for other models
