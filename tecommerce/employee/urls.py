from rest_framework import routers
from employee import views

router = routers.DefaultRouter()
router.register('employees', views.EmployeeViewSet)

urlpatterns = router.urls