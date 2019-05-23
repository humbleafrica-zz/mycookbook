import os
import datetime


AWS_ACCESS_KEY_ID = "AKIAIHWTFNXH77RS36XQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = 'thecookbookbucket'
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

S3DIRECT_REGION = 'us-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

MEDIA_ROOT = MEDIA_URL

STATICFILES_DIRS = [
    os.path.join('recipes/static'),
]

STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}