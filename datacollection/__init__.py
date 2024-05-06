@classmethod
def upload_to_s3(cls, pulse_type_file, tongue_type_file, unqiue_key):
        """
        Upload files to AWS S3 and return URLs.
        """
        # Testing please remove
        unique_key = '29-2024-12'
        # Code comes here to extract weeek-year from unique key
        folder  = '29-2024'
        s3 = boto3.client('s3')
        now = datetime.now()
        week_number = now.isocalendar()[1]
        year = now.year
        week_year_str = f"{week_number}-{year}"
        bucket_name = 'testoohybucket'
        
        # Create pulse file
        pulse_file_key = f'tongue_images/{week_year_str}/{pulse_type_file.name}'
        s3.upload_fileobj(pulse_type_file, bucket_name, pulse_file_key)
        pulse_file_url = f'https://{bucket_name}.s3.amazonaws.com/{pulse_file_key}'
        
        # Create tongue file
        tongue_file_key = f'tongue_images/{week_year_str}/{tongue_type_file.name}'
        s3.upload_fileobj(tongue_type_file, bucket_name, tongue_file_key)
        tongue_file_url = f'https://{bucket_name}.s3.amazonaws.com/{tongue_file_key}'
        
       
        return pulse_file_url, tongue_file_url

