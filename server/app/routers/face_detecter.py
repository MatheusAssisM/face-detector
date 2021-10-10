import app.controllers as controllers
from fastapi import APIRouter, UploadFile, File, Response, HTTPException


router = APIRouter(
    prefix="/face-predictor",
    responses={404: {"description": "Not found"}}
)

# Router for face recognition
@router.post(
    "/",
    responses={
        200: {"content": {"image/png": {}}},
        400: {"description": "Bad request"}
    },
    summary="Predict face"
)
async def face_recognition(image: UploadFile = File(...)):
    if not image:
        raise HTTPException(status_code=400, detail="No image provided")

    image_bytes = await image.read()
    faces = controllers.face_detecter.get_faces(image_bytes)
    return {"faces": faces}
    # return Response(content=faces[0], media_type="image/png")



