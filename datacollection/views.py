from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import DatacollectionModel
from django.http import HttpResponseBadRequest
import logging


@api_view(['POST'])
def create_objects(request):
    if request.method == 'POST':
        pulse_file = request.FILES.get('pulse_file')
        tongue_file = request.FILES.get('tongue_file')
        pulse_type = request.data.get('pulse_type')
        tongue_type = request.data.get('tongue_type')

        try:
            if not all([pulse_file, tongue_file, pulse_type, tongue_type]):
                raise ValueError("All fields are required")

            if not pulse_file.name.endswith('.csv'):
                raise ValidationError("Pulse file must be a CSV file")
            if not tongue_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError("Tongue file must be an image file (PNG, JPG, JPEG)")

            data_collection_instance = DatacollectionModel(pulse_type=pulse_type, tongue_type=tongue_type)
            data_collection_instance.process_data(pulse_file, tongue_file)

            return HttpResponse("File URLs saved successfully.", status=201)

        except (ValueError, ValidationError) as e:
            return HttpResponseBadRequest(str(e))
        except Exception as e:
            return HttpResponse("Failed to upload files and save data: {}".format(e), status=500)

    else:
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