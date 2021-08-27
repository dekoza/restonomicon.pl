from rest_framework import viewsets

from . import models, serializers


class FriendViewSet(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer


class BelongingViewSet(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.LoanSerializer
