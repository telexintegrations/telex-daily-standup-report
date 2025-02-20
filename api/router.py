from fastapi import APIRouter

from api.routes import remainder

api_router = APIRouter()
api_router.include_router(remainder.router, prefix="", tags=["tick"])
