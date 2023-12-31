from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from milhas.views import DepoimentosViewSet, DepoimentosHomeViewSet

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')
router.register('depoimentos-home', DepoimentosHomeViewSet, basename='Depoimentos-Home')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
