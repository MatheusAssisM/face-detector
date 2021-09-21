from fastapi import FastAPI
import app.routers as routers


app = FastAPI()

#routes
app.include_router(routers.face_recognition.router)


@app.get("/")
async def root():
    return {"message": "Welcome"}
