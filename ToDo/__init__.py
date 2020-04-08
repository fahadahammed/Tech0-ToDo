import os
import json
from flask import Flask
from ToDo.Configuration.configuration import configure_app, LOGGING_CONFIG
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# Logging
from logging.config import dictConfig
dictConfig(LOGGING_CONFIG)

# Initiate App
app = Flask(__name__,
            instance_relative_config=True,
            template_folder='templates')

# Configuration
configure_app(app)


# Caching
from flask_caching import Cache
ncache = Cache(app, config={'CACHE_TYPE': app.config.get('CACHE_TYPE'),
                            'CACHE_REDIS_HOST': app.config.get('CACHE_REDIS_HOST'),
                            'CACHE_REDIS_PORT': app.config.get('CACHE_REDIS_PORT'),
                            'CACHE_REDIS_DB': app.config.get('CACHE_REDIS_DB'),
                            'CACHE_KEY_PREFIX': app.config.get('CACHE_KEY_PREFIX'),
                            'CACHE_DEFAULT_TIMEOUT': app.config.get('CACHE_DEFAULT_TIMEOUT')
                            })


# Basic Auth
auth = HTTPBasicAuth()
usersObject = json.load(open(str(os.getcwd()) + "/ToDo/Configuration/users.json"))
users = {}
for i in usersObject:
    users[i] = generate_password_hash(usersObject[i])


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    else:
        return False


# Limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["3000 per minute", "500 per second"],
)


# Extras
os.makedirs(str(os.path.abspath(path="./"))+"/"+app.config["PROTECTED_PATH"], exist_ok=True)


# Routes
from ToDo.Views import _v_Home, _v_ToDo