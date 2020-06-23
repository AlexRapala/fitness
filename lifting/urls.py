from django.urls import include, path
from rest_framework import routers
from lifting import views

router = routers.DefaultRouter()
router.register('logs', views.LogViewSet, basename="logs")
router.register('lifts', views.LiftViewSet, basename="lifts")
router.register('log_x_lift', views.LogXLiftViewSet, basename="logxlift")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]