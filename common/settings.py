import pathlib


def strtobool(val):
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return 1
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return 0
    else:
        raise ValueError("invalid truth value %r" % (val,))

from pydantic_settings import BaseSettings
import environ

BASE_DIR = pathlib.Path(__file__).parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

class Settings(BaseSettings):
    debug: bool = env('DEBUG', cast = strtobool, default = False)

settings = Settings()

print(settings.debug, BASE_DIR)