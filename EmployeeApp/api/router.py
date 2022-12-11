from rest_framework.routers import DefaultRouter
from EmployeeApp.api.views import EmployeeApiViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='employee', basename='employee', viewset=EmployeeApiViewSet)