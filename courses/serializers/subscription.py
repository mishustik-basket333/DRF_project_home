from courses.models import Subscription
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
