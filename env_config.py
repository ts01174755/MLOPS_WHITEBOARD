print('\n#################### env_config.py ####################')
import subprocess

####################################################################################################
# 設定使用者相關資訊
USER_NAME = subprocess.check_output("whoami").decode('utf-8').strip()
USER_ROOT = f"/Users/{USER_NAME}"

####################################################################################################
# 設定 Project 相關資訊
## Project Name(自動取得資料夾名稱)
PROJECT_NAME = subprocess.check_output("pwd").decode('utf-8').strip().split('/')[-1]

## Project Path
PROJECT_ROOT_PATH = f'{USER_ROOT}/Development/pyDev/{PROJECT_NAME}'

## Project Local Package
PROJECT_LOCAL_PIP_INSTALL_PYTHON_PACKAGE = [
    'python-dotenv', 'psycopg2-binary', 'sqlalchemy', 'pymongo', 'fastapi', 'Jinja2==3.1.2',
    'uvicorn[standard]', 'aiofiles', 'requests', 'beautifulsoup4', 'pandas', 'black',
    'setuptools', 'build', 'pdfplumber', 'pypdf2', 'openpyxl',
    '--upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"', 'selenium', 'jupyter',
    'google-api-python-client', 'google-auth', 'google-auth-httplib2', 'google-auth-oauthlib', 'oauth2client'
]
PROJECT_LOCAL_BREW_INSTALL_PACKAGE = ['smartmontools', 'tree']

####################################################################################################
# 設定 Docker 相關資訊
## MongoDB & Mongo Express
IMAGE_MONGODB_TAG = "mongo:5.0.15"      # image tag
CONTAINER_MONGODB_NAME = "mongodb"      # container name
CONTAINER_MONGODB_PORT_LIST = ['27017:27017']   # port mapping
CONTAINER_MONGODB_ROOT = USER_ROOT          # container root
CONTAINER_MONGODB_ROOT_MAP = PROJECT_ROOT_PATH  # container root mapping
CONTAINER_MONGO_POSTGRES_NET = "mongo-postgres-net"     # container network
CONTAINER_MONGO_ENV_DICT = {
    'MONGO_INITDB_ROOT_USERNAME': 'mongodb',
    'MONGO_INITDB_ROOT_PASSWORD': 'mongodb'
}       # container env

IMAGE_MONGODB_EXPRESS_TAG = "mongo-express:0.54.0"      # image tag
CONTAINER_MONGODB_EXPRESS_NAME = "mongo_express"        # container name
CONTAINER_MONGODB_EXPRESS_PORT_LIST = ['8081:8081']     # port mapping
CONTAINER_MONGODB_EXPRESS_ROOT = USER_ROOT        # container root
CONTAINER_MONGODB_EXPRESS_ROOT_MAP = PROJECT_ROOT_PATH      # container root mapping
CONTAINER_MONGO_EXPRESS_ENV_DICT = {        
    'ME_CONFIG_MONGODB_SERVER': CONTAINER_MONGODB_NAME,
    'ME_CONFIG_MONGODB_ADMINUSERNAME': 'mongodb',
    'ME_CONFIG_MONGODB_ADMINPASSWORD': 'mongodb',
    'ME_CONFIG_BASICAUTH_USERNAME': 'mongoUser',
    'ME_CONFIG_BASICAUTH_PASSWORD': 'mongoUserPassword'
}       # container env

## Postgres & PgAdmin
IMAGE_POSTGRES_TAG = "postgres:15.2"            # image tag
CONTAINER_POSTGRES_NAME = "postgres15.2"        # container name
CONTAINER_POSTGRES_PORT_LIST = ['5432:5432']    # port mapping
CONTAINER_POSTGRES_ROOT = USER_ROOT        # container root
CONTAINER_POSTGRES_ROOT_MAP = PROJECT_ROOT_PATH     # container root mapping
CONTAINER_POSTGRES_ENV_DICT = {
    'POSTGRES_USER': 'postgres',
    'POSTGRES_PASSWORD': 'postgres',
    'POSTGRES_DB': 'postgres'
}       # container env
CONTAINER_POSTGRES_DB1 = "originaldb"       # container db1

IMAGE_PGADMIN_TAG = "dpage/pgadmin4:6.20"       # image tag
CONTAINER_PGADMIN_NAME = "pgadmin4"         # container name
CONTAINER_PGADMIN_PORT_LIST = ['5050:80']       # port mapping
CONTAINER_PGADMIN_ROOT = USER_ROOT          # container root
CONTAINER_PGADMIN_ROOT_MAP = PROJECT_ROOT_PATH      # container root mapping
CONTAINER_PGADMIN_ENV_DICT = {
    'PGADMIN_DEFAULT_EMAIL': 'pgadmin4@gmail.com',
    'PGADMIN_DEFAULT_PASSWORD': 'pgadmin4'
}       # container env
