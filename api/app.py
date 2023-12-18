from fastapi import FastAPI

from common.settings import settings
def create_app():
    app = FastAPI(
        debug = settings.debug,
        docs_url = '/docs',
        title = 'Index Page ' + str(settings.debug)
    )
    return app