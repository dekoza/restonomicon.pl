from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from . import models


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = ("id", "name", "has_overdue")


class BelongingSerializer(FlexFieldsModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Belonging
        fields = ("id", "name", "owner")


class LoanSerializer(FlexFieldsModelSerializer):
    expandable_fields = {
        "what": (BelongingSerializer, {"source": "what"}),
        "to_who": (FriendSerializer, {"source": "to_who"}),
    }

    class Meta:
        model = models.Loan
        fields = ("id", "what", "to_who", "when", "returned")
