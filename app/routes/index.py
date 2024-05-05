from fastapi import APIRouter

api_router = APIRouter()

# Principal page
@api_router.get("/")
async def root():
    return {"message": "SOAP Web Service",
            "route": "/wssound/?wsdl"}