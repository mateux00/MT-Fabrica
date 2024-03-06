from rest_framework.routers import DefaultRouter
from .viewsets import PesossaViewSet
from django.urls import include, path


router = DefaultRouter()

router.register(prefix="pessoa", viewset= PesossaViewSet)

urlpatterns = [
    path("api/",include(router.urls))

]