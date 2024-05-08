from django.db import models
from django.core.exceptions import ValidationError
from .utils import upload_to_s3, generate_unique_id

def default_pulse_file():
    return 'default_value.csv'

def default_tongue_file():
    return 'default_image.jpg' 

class DatacollectionModel(models.Model):
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
    
    def process_data(self, pulse_file, tongue_file):
        try:
            unique_id = generate_unique_id()
            pulse_file_url, tongue_file_url = upload_to_s3(pulse_file, tongue_file, unique_id)
            self.pulse_file = pulse_file_url
            self.tongue_file = tongue_file_url
            self.unique_id = unique_id
            self.save()
        except Exception as e:
            raise ValidationError(str(e))
