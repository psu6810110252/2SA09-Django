from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('shop.urls')),
    path('api/', include('cart.urls')),
    path('api/', include('orders.urls')),
    path('api/health', lambda r: JsonResponse({'status': 'OK'})),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)