from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from loguru import logger

from src.config.env import Config
from src.config.loguru import logger_config
from src.entrypoints import router
from src.middleware.logger_middleware import LoggerMiddleware
from src.utils.dependencies import api_key_dependency

APP_ROOT = Path(__file__).parent
logger.configure(**logger_config())


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("starting up")
    yield
    logger.info("shutting down")


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    _app = FastAPI(
        title="fastapi-backend-template",
        description="FastAPI backend template.",
        lifespan=lifespan,
        # default_response_class=JSONResponse,
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    _app.add_middleware(
        SQLAlchemyMiddleware,
        db_url=Config.DATABASE.DB_URL,
        engine_args=Config.DATABASE.ENGINE_ARGS,
        commit_on_exit=True,
    )
    _app.add_middleware(
        LoggerMiddleware,
        logger=logger,
    )
    _app.include_router(router=router, dependencies=[Depends(api_key_dependency)])

    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    return _app
