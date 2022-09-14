import os
ENV = os.environ.get('APP_ENV', 'dev_local')

FLASK_DEBUG_PORT = 5000

if ENV in ('dev_local', 'dev_docker', 'stg'):
    if ENV in ('dev_local', 'stg'):
        PG_HOST = 'localhost'
    elif ENV == 'dev_docker':
        PG_HOST = 'db'

    PG_USER = 'postgres'
    # PG_PASSWORD = 'password'
    PG_PASSWORD = 'postgres'
    PG_DB = 'hikma-db'
    FLASK_DEBUG = True
    PHOTOS_STORAGE_BUCKET = 'dev-api-photos'
    EXPORTS_STORAGE_BUCKET = 'dppo-hikma-api-exports'
    LOCAL_PHOTO_STORAGE_DIR = '/tmp/hikma_photos'
    DEFAULT_PROVIDER_ID_FOR_IMPORT = 'bd227f3d-0fbb-45c5-beed-8ce463481415'

if ENV == 'prod':
    FLASK_DEBUG = False
    PG_USER = 'hikma_prod'
    PG_PASSWORD = os.environ['DB_PASSWORD']
    PG_HOST = '10.114.32.2'
    PG_DB = 'hikma-prod'
    PHOTOS_STORAGE_BUCKET = os.environ['PHOTOS_STORAGE_BUCKET']
    EXPORTS_STORAGE_BUCKET = os.environ['EXPORTS_STORAGE_BUCKET']
    LOCAL_PHOTO_STORAGE_DIR = '/tmp/hikma_photos'
    DEFAULT_PROVIDER_ID_FOR_IMPORT = os.environ['DEFAULT_PROVIDER_ID']