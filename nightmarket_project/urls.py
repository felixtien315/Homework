from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nightmarket.urls')),  # 主頁包含 nightmarket 的 URL
]