from fastapi import APIRouter, UploadFile, File, Response
import io
import app.controllers as controllers


router = APIRouter(
    prefix="/face_predictor",
    responses={404: {"description": "Not found"}}
)


'''
    Router for face recognition
'''
@router.post(
    "/",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response
)
async def face_recognition(image: UploadFile = File(...)):
    if not image:
        return {"error": "No image file provided"}
    result = controllers.face_detecter.get_faces(await image.read())
    return Response(content=result, media_type="image/png")
