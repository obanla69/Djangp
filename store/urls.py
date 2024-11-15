from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from . import views

router = DefaultRouter()
router.register("collections", views.CollectionViewSet, basename="collections")
router.register("products", views.ProductViewSet, basename="products")
router.register("carts", views.CartViewSet, basename="carts")
product_router = NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", views.ReviewViewSet, basename="product-review")

print(router.urls)

urlpatterns = router.urls + product_router.urls

# products/1/reviews
# products/1/reviews/1

# urlpatterns = [
#     path('', include(product_router.urls)),
#
#
#
# path('products/', views.ProductListAPIView.as_view()),
# path('products/<int:pk>/', views.ProductDetailAPIView.as_view()),
#
# # to put everything in one Line
# path('collections', views.CollectionListAPIView.as_view()),
# path('collections/<int:pk>', views.CreateCollectionSerializer, name='collection-detail'),
#
# ]
