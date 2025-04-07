from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyse/', include('analyse.urls')),
    # path('caisse/', include('caisse.urls')),
    # path('utilisateur/', include('utilisateur.urls')),
    path('', include('analyse.urls')),#inclure votre application ici
]