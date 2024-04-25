from rest_framework import serializers
from api.models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['uid','reg','compt','status']