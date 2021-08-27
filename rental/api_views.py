import django_filters
import pendulum
from django.core.mail import send_mail
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from . import models, serializers
from .permissions import IsOwner


class FriendViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
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


class LoanViewSet(NestedViewSetMixin, FlexFieldsModelViewSet):
    queryset = models.Loan.objects.all().select_related("to_who", "what")
    permit_list_expands = ["what", "to_who"]
    serializer_class = serializers.LoanSerializer
    filterset_class = LoanFilterSet

    @action(detail=True, url_path="remind", methods=["post"])
    def remind_single(self, request, *args, **kwargs):
        obj = self.get_object()
        send_mail(
            subject=f"Proszę oddaj moją własność: {obj.what.name}",
            message=f'Chyba zapominasz o zwrocie mojej własności: "{obj.what.name}"" pożyczonej dnia {obj.when}. Proszę o zwrot.',
            from_email="me@example.com",  # tutaj podaj swojego maila
            recipient_list=[obj.to_who.email],
            fail_silently=False,
        )
        return Response("Email wysłany.")
