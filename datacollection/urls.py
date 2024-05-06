from django.urls import path
from . import views

urlpatterns = [
    # Endpoint to retrieve file data
    path('retrieve_file_data/', views.retrieve_file_data, name='retrieve_file_data'),
    
    # Endpoint to create objects
    path('create_objects/', views.create_objects, name='create_objects'),
]
