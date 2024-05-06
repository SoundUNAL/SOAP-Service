from fastapi import FastAPI
from routes.index import api_router
from controllers.wssound import soap_router

app = FastAPI()

# routes
app.include_router(api_router)
app.include_router(soap_router)