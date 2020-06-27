from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = []

app_name = 'authentication'
urlpatterns += router.urls
urlpatterns += [
    path('v1/auth/', include('rest_framework_social_oauth2.urls')),
]