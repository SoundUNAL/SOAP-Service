from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Soap Web Service",
            "route": "/soap-service-route"}