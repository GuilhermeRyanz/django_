from rest_framework import routers
from sale import views

router = routers.DefaultRouter()
router.register('sale', views.SalesViewSet)

urlpatterns = router.urls