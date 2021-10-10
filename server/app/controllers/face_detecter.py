import app.services.face_detecter as face_detecter
from fastapi import HTTPException

'''
    Get faces from a image
'''
def get_faces(image):
    try:
        result = face_detecter.get_faces(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail='Sorry, something wrong!')
    return result
