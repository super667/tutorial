from .models import CustomerReportRecord
from rest_framework import serializers

class CustomerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReportRecord
        fields = "__all__"


from rest_framework.validators import UniqueValidator
