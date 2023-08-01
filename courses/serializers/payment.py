from rest_framework import serializers

from courses.models import Payment, Course, Lesson


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
