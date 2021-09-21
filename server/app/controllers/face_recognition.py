import app.services.face_recognition as face_recognition

'''
    Get faces from a image
'''
def get_faces(image):
    result = face_recognition.get_faces(image)
    return result
