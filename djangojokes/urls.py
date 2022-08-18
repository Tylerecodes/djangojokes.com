from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # User Management
    path('account/', include('allauth.urls')),

    # Admin
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    # Local Apps
    path('jobs/', include('jobs.urls')),
    path('jokes/', include('jokes.urls')),
    path('', include('pages.urls')),
]
