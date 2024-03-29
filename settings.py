import os
from dotenv import load_dotenv
from datetime import timedelta
load_dotenv()

''' Application '''
# Set application root, default value js '/'
APPLICATION_ROOT = '/'

''' Session '''
# Secret key setting from .env for Flask sessions
SECRET_KEY = os.environ.get('SECRET_KEY')
# Set session lifetime, default value js timedelta(days=31)
#   see: https://docs.python.org/3/library/datetime.html#datetime.timedelta
PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)

''' Database '''
# DB base configuration from .env for modularity and security reasons
DB = {
    'uri': os.environ.get('DB_URI'),
    'database': os.environ.get('DB_NAME')
}
