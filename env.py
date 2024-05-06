from dotenv import load_dotenv
import os

load_dotenv()

DATA_COLLECTION_BUCKET = os.environ.get("DATA_COLLECTION_BUCKET", "")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_SECRET_ACCESS_KEY= os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_S3_REGION_NAME =  os.environ.get("AWS_S3_REGION_NAME", "")
AWS_S3_SIGNATURE_NAME =  os.environ.get("AWS_S3_SIGNATURE_NAME", "")
HOST = os.environ.get("HOST", "")
NAME= os.environ.get("NAME", "")