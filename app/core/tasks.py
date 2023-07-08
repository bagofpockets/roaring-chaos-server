import os
from logging import getLogger
from typing import Callable
from fastapi.applications import FastAPI

logger = getLogger(__name__)


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        logger.info('Starting...')

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        logger.info('Stopping...')

    return stop_app
