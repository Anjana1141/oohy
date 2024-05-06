from django.db import models
from django.core.exceptions import ValidationError
from .utils import upload_to_s3, generate_unique_id

def default_pulse_file():
    """
    Default file for pulse type.
    
    Returns:
        str: Default file name for pulse type.
    """
    return 'default_value.csv'

def default_tongue_file():
    """
    Default file for tongue type.
    
    Returns:
        str: Default file name for tongue type.
    """
    return 'default_image.jpg' 

class DatacollectionModel(models.Model):
    """
    Model to collect data related to pulse and tongue types.
    """
    PULSE_TYPE_CHOICES = [
        (1, 'Wind'),
        (2, 'Humid'),
        (3, 'Cold'),
    ]
    TONGUE_TYPE_CHOICES = [
        (1, 'Tongue type 1'),
        (2, 'Tongue type 2'),
        (3, 'Tongue type 3'),
    ]

    pulse_file = models.FileField(upload_to='pulse_file/', default=default_pulse_file)
    tongue_file = models.ImageField(upload_to='tongue_file/', default=default_tongue_file)
    unique_id = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pulse_type = models.IntegerField(choices=PULSE_TYPE_CHOICES)
    tongue_type = models.IntegerField(choices=TONGUE_TYPE_CHOICES)
    
    def processData(self, pulse_file, tongue_file):
        """
        Upload files to S3, save data, and insert into MongoDB.
        
        Args:
            pulse_file: File object for pulse data.
            tongue_file: File object for tongue data.
        
        Raises:
            ValidationError: If an error occurs during the process.
            Exception: For any other unexpected errors.
        """
        try:
            # Generate a unique ID for the data
            unique_id = generate_unique_id()
            # Upload pulse and tongue files to S3 and get their URLs
            pulse_file_url, tongue_file_url = upload_to_s3(pulse_file, tongue_file, unique_id)
            # Assign the URLs and unique ID to the instance attributes
            self.pulse_file = pulse_file_url
            self.tongue_file = tongue_file_url
            self.unique_id = unique_id
            # Save the instance
            self.save()
        except ValueError as ve:
            # If a ValueError occurs, raise a ValidationError
            raise ValidationError(str(ve))
        except Exception as e:
            # If any other exception occurs, raise it
            raise e
