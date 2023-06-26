import os

from fastapi_login import LoginManager


class NotAuthenticatedException(Exception):
    pass


# create login manager
manager = LoginManager(os.urandom(24).hex(),
                       token_url='auth/token')
manager.not_authenticated_exception = NotAuthenticatedException

