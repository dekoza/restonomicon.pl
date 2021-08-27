import django_filters
import pendulum
from rest_framework import viewsets

from . import models, serializers
from .permissions import IsOwner


class FriendViewSet(viewsets.ModelViewSet):
    queryset = models.Friend.objects.with_overdue()
    serializer_class = serializers.FriendSerializer


class BelongingViewSet(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer
    permission_classes = [IsOwner]


class LoanFilterSet(django_filters.FilterSet):
    missing = django_filters.BooleanFilter(field_name="returned", lookup_expr="isnull")
    overdue = django_filters.BooleanFilter(method="get_overdue", field_name="returned")

    class Meta:
        model = models.Loan
        fields = ["what", "to_who", "missing", "overdue"]

    def get_overdue(self, queryset, field_name, value):
        if value:
            return queryset.filter(when__lte=pendulum.now().subtract(months=2))
        return queryset


class LoanViewSet(viewsets.ModelViewSet):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.LoanSerializer
    filterset_class = LoanFilterSet
