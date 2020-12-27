from django.conf.urls import include, url
from .views import (
    ClientCrud,
    QualityLotCrud,
    ProductCrud,
    OrderCrud,
    OrderView
)
from rest_framework.routers import DefaultRouter
from importlib.resources import path

router = DefaultRouter()
router.register(r'client', ClientCrud, basename='client')
router.register(r'quality_lot', QualityLotCrud, basename='quality_lot')
router.register(r'product', ProductCrud, basename='product')
router.register(r'order', OrderCrud, basename='order')
router.register(r'order-list', OrderView, basename='order')
urlpatterns = router.urls