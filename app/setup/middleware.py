from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette_context import plugins
from starlette_context.middleware import RawContextMiddleware

# TODO: Add traffic logging middleware # pylint: disable=fixme
middlewares = [
    Middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]),
    Middleware(
        RawContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),  # for X-Request-ID inside of starlette_context.context
            plugins.CorrelationIdPlugin(),  # for X-Correlation-ID of starlette_context.context
        ),
    ),
    Middleware(GZipMiddleware, minimum_size=1000),
]
