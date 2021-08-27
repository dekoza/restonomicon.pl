from rest_framework import serializers

from . import models


class FriendSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Friend
        fields = ("id", "name")


class BelongingSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Belonging
        fields = ("id", "name")


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Loan
        fields = ("id", "what", "to_who", "when", "returned")
