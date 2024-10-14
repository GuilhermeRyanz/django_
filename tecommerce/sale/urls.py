from rest_framework import routers
from sale import views

router = routers.DefaultRouter()
router.register('sales', views.SalesViewSet)

urlpatterns = router.urls