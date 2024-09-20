import json
import boto3
import urllib.parse
import logging


# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the Glue client
glue_client = boto3.client('glue')

def handler(event, context):
    # Log the incoming event for debugging
    logger.info("Received event: " + json.dumps(event, indent=2))

    # Retrieve the bucket name and object key from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    logger.info(f"File uploaded to bucket: {bucket_name}, key: {object_key}")

    # Start the Glue ETL job (replace 'my-glue-job' with your actual Glue job name)
    try:
        validate_file_extension(object_key)
        response = glue_client.start_job_run(
            JobName='garmin_etl_job',  # Your Glue job name
            Arguments={
                '--S3Bucket': bucket_name,
                '--S3Key': object_key
            }
        )
        logger.info(f"Started Glue job: {response['JobRunId']}")
    except Exception as e:
        logger.error(f"Error starting Glue job: {str(e)}")
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully.')
    }   

def validate_file_extension(object_key, allowed_extensions=['.csv']):
    # Check if the file has the correct extension
    if not any(object_key.endswith(ext) for ext in allowed_extensions):
        raise ValueError(f"Invalid file type for key {object_key}. Allowed: {allowed_extensions}")
