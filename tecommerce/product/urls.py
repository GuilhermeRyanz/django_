from rest_framework import routers
from product import views

router = routers.DefaultRouter()

router.register('products', views.ProductViewSet)

urlpatterns = router.urls