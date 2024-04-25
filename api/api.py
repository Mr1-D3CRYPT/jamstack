from api.models import Complaint
from rest_framework import viewsets, permissions
from .serializers import ComplaintSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ComplaintSerializer