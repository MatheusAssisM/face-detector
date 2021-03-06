import app.services.face_detector as face_detector
from fastapi import HTTPException

'''
    Get faces from a image
'''
def get_faces(image):
    try:
        result = face_detector.get_faces(image)
        return result
    except Exception as e:
        if type(e) is not HTTPException:
            print(e)
            raise HTTPException(status_code=500, detail='Something wrong!')
        else:
            raise e

