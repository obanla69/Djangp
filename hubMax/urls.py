
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls


admin.site.site_header = 'HubMax Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('demo/', include("demo.urls")),
    path("store/", include("store.urls")),
    # path("user/",include("user.urls")),

]+ debug_toolbar_urls()
