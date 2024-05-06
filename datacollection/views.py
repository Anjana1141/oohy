from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import DatacollectionModel
from django.http import HttpResponseBadRequest
import logging


@api_view(['POST'])
def create_objects(request):
    """
    API view to create DatacollectionModel instances.

    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        Response: Response indicating success or failure.
    """
    if request.method == 'POST':
        pulse_file = request.FILES.get('pulse_file')
        tongue_file = request.FILES.get('tongue_file')
        pulse_type = request.data.get('pulse_type')
        tongue_type = request.data.get('tongue_type')

        try:
            if not pulse_file:
                raise ValueError("No pulse file provided")
            if not tongue_file:
                raise ValueError("No tongue file provided")
            if pulse_type is None:
                raise ValueError("No pulse type provided")
            if tongue_type is None:
                raise ValueError("No tongue type provided")

            # Check file types
            if not pulse_file.name.endswith('.csv'):
                raise ValidationError("Pulse file must be a CSV file")
            if not tongue_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError("Tongue file must be an image file (PNG, JPG, JPEG)")

            # Create a new instance of DatacollectionModel
            data_collection_instance = DatacollectionModel(
                pulse_type=pulse_type,
                tongue_type=tongue_type
            )
            
            # Call the processData method on the instance
            data_collection_instance.processData(pulse_file, tongue_file)

            return HttpResponse("File URLs saved successfully.", status=201)  # 201 Created
        
        except (ValueError, ValidationError) as e:
            # If a ValueError or ValidationError occurs, return a bad request response
            return HttpResponseBadRequest(str(e))
        
        except Exception as e:
            # If any other exception occurs
            if 'Mongo' in str(e):
                # Check if it's a database server error
                return HttpResponse("Database server error.", status=503)  # 503 Service Unavailable
            else:
                # If not a database server error, assume it's an issue with AWS file storing
                return HttpResponse("Failed to upload files and save data: Files didn't save to AWS server.", status=500)
                # 500 Internal Server Error
        
    else:
        # If the request method is not POST, return a method not allowed response
        return HttpResponse("This endpoint only accepts POST requests.", status=405)
    
@api_view(['GET'])
def retrieve_file_data(request):
        """
        API view to retrieve file data.

        Args:
            request (HttpRequest): HTTP request object.

        Returns:
            Response: Response indicating success or failure.
        """
        try:
            # Your code for retrieving file data
            return Response({'status': 'Not implemented'}, status=501)  # 501 Not Implemented
        except Exception as e:
            # If an exception occurs, return a server error response
            return Response({'status': 'Error retrieving file data', 'error': str(e)}, status=500)  # 500 Internal Server Error