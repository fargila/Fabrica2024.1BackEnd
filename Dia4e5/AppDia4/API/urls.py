from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import ViaCepModel
from django.contrib import admin

router = DefaultRouter()
router.register("ViaCep", ViaCepModel)

urlpatterns = [
    path('api/', router.site.urls),

]