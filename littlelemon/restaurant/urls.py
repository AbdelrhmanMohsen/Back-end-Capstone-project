from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

# Print router URLs
for url in router.urls:
    print(url)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('bookings/', include(router.urls)),  # Include router URLs without a name
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),
]

