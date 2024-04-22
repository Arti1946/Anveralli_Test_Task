from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("orders/", include("orders.urls")),
    path("auth/", include("users.urls"), name="users"),
    path("admin/", admin.site.urls),
    path("auth/", include("django.contrib.auth.urls")),
]
