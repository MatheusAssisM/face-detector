import app.services.face_detecter as face_detecter
from fastapi import HTTPException

'''
    Get faces from a image
'''
def get_faces(image):
    try:
        result = face_detecter.get_faces(image)
    except Exception as e:
        print(e)
    return result
