from fastapi import FastAPI, APIRouter
import os

# prefix: used if i want a certain prefix for the website, meaning that no one can access this Route expecpt after typing this prefix in the URL (URL/prefix)
# tags: used in docs and postman for ordering the Routes (grouping certain routes together)
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

# default route
# used in health checks by devops and other uses
@base_router.get("/")
async def welcome():
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')
    
    return {
        "app name": app_name,
        "app version": app_version,
    }
