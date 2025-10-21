from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from modules.add_ons import add_ons_router
from modules.plans import plan_router
from modules.texts import text_router

app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
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
app.include_router(add_ons_router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
