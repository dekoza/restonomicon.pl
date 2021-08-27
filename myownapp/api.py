from rest_framework import routers

from rental import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r"friends", myapp_views.FriendViewSet)
router.register(r"belongings", myapp_views.BelongingViewSet)
router.register(r"loans", myapp_views.LoanViewSet)
