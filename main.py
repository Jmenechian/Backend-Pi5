from fastapi import FastAPI

from router.router import router  

app = FastAPI(title="PI5 API", version="1.0.0")

app.include_router(router)