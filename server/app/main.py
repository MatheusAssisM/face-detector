from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.routers as routers


app = FastAPI()

allowed_origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#routes
app.include_router(routers.face_detecter.router)


@app.get("/")
async def root():
    return {"message": "Welcome"}
