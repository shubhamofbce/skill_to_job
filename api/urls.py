from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('1.0/', include('api.v_1_0.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth-token/', views.obtain_auth_token)
]