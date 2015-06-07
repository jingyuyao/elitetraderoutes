from django.contrib.auth.models import User

from rest_framework import serializers

class IDHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    Just a normal HyperlinkedModelSerializer with an ID field.
    """
    id = serializers.ReadOnlyField()

class UserSerializer(IDHyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username',)