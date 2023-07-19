from django.test import TestCase
import boto3
import os
import dotenv
from botocore.exceptions import NoCredentialsError
  

dotenv.load_dotenv()
def test_s3_connection():
    # Specify the name of the S3 bucket
    bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')

    # Specify the local file path of the test file to be uploaded
    local_file_path = 'requirements.txt'

    # Specify the desired S3 object key for the uploaded file
    s3_object_key = 'requirements.txt'

    try:
        # Create an S3 client using your AWS credentials
        s3_client = boto3.client('s3',
                                 aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                 aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

        # Upload the test file to the S3 bucket
        s3_client.upload_file(local_file_path, bucket_name, s3_object_key)

        # Print success message if the file was uploaded
        print(f"Test file uploaded to S3 bucket: {bucket_name}")

    except NoCredentialsError:
        # Print error message if AWS credentials are missing or incorrect
        print("AWS credentials not found or invalid")


test_s3_connection()