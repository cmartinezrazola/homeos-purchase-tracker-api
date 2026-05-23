from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import (
    MarketplaceViewSet,
    OrderViewSet,
    OrderItemViewSet,
)

router = DefaultRouter()

router.register(r'marketplaces', MarketplaceViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = router.urls 

# order_list = OrderViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# order_detail = OrderViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# urlpatterns = [
#     path('orders/', order_list),
#     path('orders/<int:pk>/', order_detail),
# ]

