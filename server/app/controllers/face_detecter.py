import app.services.face_detecter as face_detecter

'''
    Get faces from a image
'''
def get_faces(image):
    result = face_detecter.get_faces(image)
    return result
