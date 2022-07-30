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
    PG_DB = 'hikma_dev'
    FLASK_DEBUG = True
    PHOTOS_STORAGE_BUCKET = 'dev-api-photos'
    EXPORTS_STORAGE_BUCKET = 'dppo-hikma-api-exports'
    LOCAL_PHOTO_STORAGE_DIR = '/tmp/hikma_photos'
    DEFAULT_PROVIDER_ID_FOR_IMPORT = 'bd227f3d-0fbb-45c5-beed-8ce463481415'

if ENV == 'prod':
    FLASK_DEBUG = False
    PG_USER = 'hikma_prod'
    PG_PASSWORD = 'pmy"8,*Rq4$a.?J:'
    PG_HOST = 'localhost'
    PG_DB = 'hikma_prod'
    PHOTOS_STORAGE_BUCKET = 'dppo-hikma-photos-exports'
    EXPORTS_STORAGE_BUCKET = 'dppo-hikma-api-exports'
    LOCAL_PHOTO_STORAGE_DIR = '/tmp/hikma_photos'
    DEFAULT_PROVIDER_ID_FOR_IMPORT = os.environ['DEFAULT_PROVIDER_ID']