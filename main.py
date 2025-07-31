from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import text_routes, plan_routes, add_ons_routes

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

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(text_routes.router)
app.include_router(plan_routes.router)
app.include_router(add_ons_routes.router)
