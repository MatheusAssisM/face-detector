from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.routers as routers


app = FastAPI()

allowed_origins = [
    "http://localhost:3000",
    "https://2c8b-2804-dd4-807a-6000-f960-a76d-9712-304e.ngrok.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

#routes
app.include_router(routers.face_detecter.router)


@app.get("/")
async def root():
    return {"message": "Welcome"}
