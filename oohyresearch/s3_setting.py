# s3_settings.py
# import os
# from storages.backends.s3boto3 import S3Boto3Storage


# # AWS S3 settings
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('YOUR_AWS_STORAGE_BUCKET_NAME')
# AWS_S3_REGION_NAME = 'ap-south-1'

# # For static files
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'

# # For media files
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'

# # # Optional: Custom storage classes for different purposes
# # class StaticRootS3Boto3Storage(S3Boto3Storage):
# #     location = 'static'

# class MediaRootS3Boto3Storage(S3Boto3Storage):
#     location = 'media'
