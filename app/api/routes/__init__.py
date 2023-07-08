from fastapi import APIRouter
from api.routes.health import router as health_router
from api.routes.qa import router as qa_router

router = APIRouter()

router.include_router(health_router, tags=["Health"])
router.include_router(qa_router, tags=["QA"])
