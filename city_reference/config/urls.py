from django.contrib import admin
from django.urls import path

from core.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path("moscow",main, name = "Москва"),
    path("spb",main, name = "Санкт-Петербург"),
    path("saratov", main, name = "Саратов"),
    path("kazan", main, name = "Казань"),
    path("samara", main, name = "Самара"),
    path("ekb", main, name = "Екатеринбург")
]
