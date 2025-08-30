from django.urls import path, include
from .views import PropertyListView
from django.contrib import admin

urlpatterns = [
    path('', PropertyListView.as_view(), name='property_list'),
    path('admin/', admin.site.urls),
    path('properties/', include('properties.urls')),
]
