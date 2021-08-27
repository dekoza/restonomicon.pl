from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from rental import api_views as myapp_views


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()

friends = router.register(r"friends", myapp_views.FriendViewSet)
friends.register(
    r"loans",
    myapp_views.LoanViewSet,
    basename="friends-loan",
    parents_query_lookups=["to_who"],
)

router.register(r"belongings", myapp_views.BelongingViewSet)
router.register(r"loans", myapp_views.LoanViewSet)
