from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from .views import update_remark, fetch_page, update_page, get_configuration

urlpatterns = [
    path('api/configurations/<str:id>', get_configuration),  # GET
    path('api/configurations/<str:id>',csrf_exempt(update_remark)),      # PUT
    path('fetch/', fetch_page),
    path('update/', update_page),
]
