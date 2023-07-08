from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core import tasks, settings
from api.routes import router as api_router
from api.logger import LoggingMiddleware


def get_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION, root_path='')
    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    app.include_router(api_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(LoggingMiddleware)

    return app


app = get_application()
