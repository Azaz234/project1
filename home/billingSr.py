from importlib.metadata import files
from rest_framework import serializers
from home.models import students
class customerserializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields="__all__"