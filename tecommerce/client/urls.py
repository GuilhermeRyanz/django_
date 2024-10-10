from rest_framework import routers
from client import views

router = routers.DefaultRouter()
router.register('clients', views.ClientViewSet)

urlpatterns = router.urls