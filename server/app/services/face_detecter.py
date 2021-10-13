import cv2
import matplotlib.image as mpimg
from fastapi import HTTPException
import io
import base64
import dlib


def get_faces(image):
    '''
        Get the faces from the image

        args:
            image(bytes): image in bytes

        Return:
            image_base64(dict): dict with the base64 encoded images and the number of faces
    '''
    check_image_size(image)
    check_format_image(image)
    face_detector = build_face_detector()
    image_resized = get_gray_image(image)
    # marked_image = _build_rectangle_on_image(image_resized, face_detector)
    faces = crop_faces(image_resized, face_detector)
    images_buffered = get_buffered_images(faces)
    images_base64 = bytes_to_base64(images_buffered)
    return images_base64

def get_gray_image(image_data):
    '''
        Resize the image to a proportion of the original image
        and convert to grayscale

        args:
            image_data(bytes): image in bytes
        
        Return:
            image_rgb(cv2): image array in grayscale
    '''
    image = mpimg.imread(io.BytesIO(image_data), format='jpeg')
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image_rgb


def resize_image(image, scale_percent=30):
    '''
        Resize the image to a proportion of the original image

        args:
            image(cv2): image (array)
            scale_percent(int): scale percentage
        
        Return:
            image_resized(cv2): image (array) resized
    '''
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image_resized = cv2.resize(
        image.copy(),
        dim,
        interpolation=cv2.INTER_AREA
    )
    return image_resized

def build_face_detector():
    '''
        Build the face detector for frontal faces

        Return:
            face_detector(dlib): Face detector from DLIB
    '''
    _classifier_68_path = './app/utils/classifiers/shape_predictor_68_face_landmarks.dat'
    dlib.shape_predictor(_classifier_68_path)
    face_detector = dlib.get_frontal_face_detector()
    return face_detector

def build_rectangle_on_image(image, face_detector):
    '''
        Mark the rectangle around the faces

        Return: 
            image(cv2): Array image with marked faces
    '''
    faces = face_detector(image, 1)
    if not faces:
        raise HTTPException(status_code=404, detail='No faces found')

    for _, d in enumerate(faces):
        cv2.rectangle(
            image, 
            (d.left(), d.top()), 
            (d.right(), d.bottom()), 
            (255, 0, 0), 
            2
        )
    return image

def get_buffered_images(images):
    '''
        Get all buffered images
    '''
    images_buffered = []
    if not images:
        raise HTTPException(status_code=404, detail='No faces found')

    for image in images:
        _, image_buffer = cv2.imencode('.jpg', image)
        images_buffered.append(image_buffer.tobytes())
    return images_buffered

def crop_faces(image, face_detector):
    '''
        Crop the faces from image

        Return:
            croped_faces(list): a list with all faces
    '''
    faces = face_detector(image, 1)
    croped_faces = []
    if not faces:
        raise HTTPException(status_code=404, detail='No faces found')

    for _, d in enumerate(faces):
        face = image[d.top():d.bottom(), d.left():d.right()]
        croped_faces.append(face)
    return croped_faces

def bytes_to_base64(images):
    '''
        Convert a image to base64 and count the total faces

        Return:
            images_base64(dict): Dict with all faces and the total faces
    '''
    images_base64 = {
        "faces_images": [],
        "faces_count": len(images)
    }
    if not images:
        raise HTTPException(status_code=404, detail='No faces found')

    for image in images:
        images_base64['faces_images'].append(base64.b64encode(image))
    
    return images_base64

def check_image_size(image):
    '''
        Check if the image is bigger than 6MB
    '''
    image_size = len(image) / 1000
    if image_size > 6000:
        raise HTTPException(
            status_code=404, 
            detail=f'Image is bigger than 6MB: {image_size / 1000}'
        )
    return

def check_format_image(image):
    '''
        Check if the image is in jpeg format
    '''
    if not image.startswith(b'\xff\xd8'):
        raise HTTPException(
            status_code=404, 
            detail='Image is not in jpeg format'
        )
    return