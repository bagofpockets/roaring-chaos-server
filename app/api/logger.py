import time
import logging
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import Send
from context import request_id


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id.get()
        record.service = 'api'
        return True


logging.basicConfig(level=logging.INFO, format='%(levelname)s UTC %(asctime)s | %(message)s')
logger = logging.getLogger(__name__)
logger.addFilter(ContextFilter())


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Send) -> None:
        start_time = time.time()
        request_headers = dict(request.headers)
        request_id.set(str(uuid.uuid4()))
        if 'cookie' in request_headers:
            del request_headers['cookie']

        logger.info(f"Request {request_id.get()} Headers: {request_headers}")

        response = await call_next(request)

        duration = time.time() - start_time
        logger.info(f"Request {request_id.get()} Duration {duration:.4f} seconds")

        return response
