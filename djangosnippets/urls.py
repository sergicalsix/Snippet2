from django.contrib import admin
from django.urls import path, include

from snippet.views import top

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top, name = 'top'),
    path('snippet/', include('snippet.urls')),
]
