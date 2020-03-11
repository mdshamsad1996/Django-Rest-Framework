from django.urls import path

from . import views


urlpatterns = [
    path('', views.EmployeeListCreatView.as_view(), name='employee_list_create'),
    path('<int:pk>/', views.EmployeeRetriveDestroyView.as_view(), name='employee_retrieve_delete'),
   
]