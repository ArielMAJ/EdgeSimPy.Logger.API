from fastapi.routing import APIRouter

from src.entrypoints import log, monitoring

router = APIRouter()
router.include_router(monitoring.router, tags=["Monitoring"])
router.include_router(log.router, prefix="/log", tags=["Logging"])

__all__ = ["router"]
