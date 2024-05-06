import boto3
import random
from datetime import datetime
from botocore.exceptions import ClientError
from env import DATA_COLLECTION_BUCKET

def generate_unique_id():
    """
    Generate a unique ID based on the current week and year.
    Create a new folder in the S3 bucket for each new week.
    Increment the serial number from the last folder's serial number.
    
    Returns:
        str: Unique ID in the format 'week-year-serial_number'.
    """
    now = datetime.now()
    week_number = now.isocalendar()[1]
    year = now.year
    week_year_str = f"{week_number}-{year}"
    
    last_serial_number = get_last_serial_number(week_number)  # Calling class method
    
    last_week = now.isocalendar()[1]  # Define last_week as the current week
    
    if last_serial_number is None:
        serial_number = 1  # Start a new series for the week
    elif last_week == week_number:
        serial_number = last_serial_number + 1  # Increment the serial number from the last folder
    elif last_week < week_number:
        serial_number = 1  # Start a new series for the week

    create_s3_folder(week_year_str)  #calling class method to create S3 folder
    
    unique_id = f"{week_year_str}-{serial_number}"
    
    return unique_id

def create_s3_folder(folder_key):
    """
    Create a new folder in the S3 bucket if it doesn't exist.
    
    Args:
        folder_key (str): Key of the folder to be created.
    """
    s3 = boto3.client('s3')
    bucket_name = DATA_COLLECTION_BUCKET

    try:
        s3.head_object(Bucket=bucket_name, Key=(folder_key + 'dummy_key'))
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            # Folder doesn't exist, create it
            s3.put_object(Bucket=bucket_name, Key=(folder_key + '/'))

def upload_to_s3(pulse_file, tongue_file, unique_key):
    """
    Upload files to AWS S3 and return URLs.
    
    Args:
        pulse_file: File object for pulse data.
        tongue_file: File object for tongue data.
        unique_key (str): Unique key used for folder structure in S3.
    
    Returns:
        Tuple[str, str]: URLs of the uploaded pulse file and tongue file.
    """
    # Logic for Extract week-year from unique key
    week_year_str = unique_key.split('-')[:-1]  # Extracting week-year part
    week_year_str = '-'.join(week_year_str)  # Joining back to get week-year string

    s3 = boto3.client('s3')
    bucket_name =  DATA_COLLECTION_BUCKET

    # Create pulse file
    if not pulse_file:
        raise ValueError("No pulse file provided")
    pulse_file_key = f'{week_year_str}/{pulse_file.name}'
    s3.upload_fileobj(pulse_file, bucket_name, pulse_file_key)
    pulse_file_url = f'https://{bucket_name}.s3.amazonaws.com/{pulse_file_key}'

    # Create tongue file
    if not tongue_file:
        raise ValueError("No tongue file provided")
    tongue_file_key = f'{week_year_str}/{tongue_file.name}'
    s3.upload_fileobj(tongue_file, bucket_name, tongue_file_key)
    tongue_file_url = f'https://{bucket_name}.s3.amazonaws.com/{tongue_file_key}'

    return pulse_file_url, tongue_file_url

def get_last_serial_number(current_week):
    """
    Get the last serial number from the previous folder.
    
    Args:
        current_week (int): Current week number.
    
    Returns:
        int or None: Last serial number from the previous folder if exists, otherwise None.
    """
    # Logic to retrieve the last serial number from the previous folder based on the current week
    # You might need to query the database to get the last recorded week and its serial number
    
    # For demonstration purposes, returning a random number
    last_serial_number = random.randint(0, 100)
    last_week = random.randint(1, 52)  # Assuming there are 52 weeks in a year
    
    if last_week < current_week:
        return last_serial_number
    else:
        return None
