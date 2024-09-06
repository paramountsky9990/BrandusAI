from django.urls import path,include
from .views import connect_social, disconnect_social, get_connected_socials

urlpatterns = [
    path('connect/<str:platform>/', connect_social, name='connect_social'),
    path('disconnect/<str:platform>/', disconnect_social, name='disconnect_social'),
    path('connected-socials/', get_connected_socials, name='get_connected_socials'),
    path('accounts/', include('allauth.urls')),

]
