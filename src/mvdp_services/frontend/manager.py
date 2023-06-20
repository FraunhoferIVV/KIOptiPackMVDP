import os

from fastapi_login import LoginManager

# create login manager
manager = LoginManager(os.urandom(24).hex(), token_url='auth/token')
