from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import add_ons_routes
from modules.plans import plan_router
from modules.texts import text_router

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://adrienb23.github.io"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(text_router.router)
app.include_router(plan_router.router)
app.include_router(add_ons_routes.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
