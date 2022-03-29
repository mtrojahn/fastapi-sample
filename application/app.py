from fastapi import FastAPI

from endpoints import symptoms


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(symptoms.router)

    return app
