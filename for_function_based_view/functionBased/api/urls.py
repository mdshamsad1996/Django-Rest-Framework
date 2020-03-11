from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.create_get_user),
    path('<int:pk>/',views.update_delete_user)
]
