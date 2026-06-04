import boto3
from botocore.exceptions import NoCredentialsError
from backend.config import Config

s3_client = boto3.client(
    "s3",
    aws_access_key_id=Config.AWS_ACCESS_KEY,
    aws_secret_access_key=Config.AWS_SECRET_KEY,
    region_name=Config.AWS_REGION
)

def upload_file(file, filename):
    try:
        s3_client.upload_fileobj(
            file,
            Config.S3_BUCKET,
            filename,
            ExtraArgs={"ContentType": file.content_type}
        )

        return f"https://{Config.S3_BUCKET}.s3.{Config.AWS_REGION}.amazonaws.com/{filename}"

    except NoCredentialsError:
        return None


def generate_presigned_url(key, expiration=3600):
    return s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": Config.S3_BUCKET, "Key": key},
        ExpiresIn=expiration
    )