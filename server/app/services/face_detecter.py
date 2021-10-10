import cv2
import matplotlib.image as mpimg
from fastapi import HTTPException
import io
import base64
import dlib

# Get faces from image
def get_faces(image):
    face_detector = _build_face_detector()
    image_resized = _get_resized_gray_image(image)
    # marked_image = _build_rectangle_on_image(image_resized, face_detector)
    faces = _crop_faces(image_resized, face_detector)
    images_buffered = _get_buffered_images(faces)
    images_base64 = _bytes_to_base64(images_buffered)
    return images_base64

# Resize image and convert to grayscale
def _get_resized_gray_image(image_data):
    image = mpimg.imread(io.BytesIO(image_data), format='jpeg')
    image_resized = _resize_image(image)
    image_rgb = cv2.cvtColor(image_resized.copy(), cv2.COLOR_BGR2GRAY)
    return image_rgb


# Resize the image to a proportion of the original image
def _resize_image(image, scale_percent=30):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image_resized = cv2.resize(
        image.copy(),
        dim,
        interpolation=cv2.INTER_AREA
    )
    return image_resized

# Build the face detector for frontal faces
def _build_face_detector():
    _classifier_68_path = './app/utils/classifiers/shape_predictor_68_face_landmarks.dat'
    dlib.shape_predictor(_classifier_68_path)
    face_detector = dlib.get_frontal_face_detector()
    return face_detector

# Build the rectangle around the faces
def _build_rectangle_on_image(image, face_detector):
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

# Get buffered jpg image 
def _get_buffered_images(images):
    images_buffered = []
    if not images:
        return HTTPException(status_code=404, detail='No faces found')

    for image in images:
        _, image_buffer = cv2.imencode('.jpg', image)
        images_buffered.append(image_buffer.tobytes())
    return images_buffered

# Crop faces from image and return the cropped image
def _crop_faces(image, face_detector):
    faces = face_detector(image, 1)
    croped_faces = []
    if not faces:
        raise HTTPException(status_code=404, detail='No faces found')

    for _, d in enumerate(faces):
        face = image[d.top():d.bottom(), d.left():d.right()]
        # resized_face = _resize_image(face)
        croped_faces.append(face)
    return croped_faces

def _bytes_to_base64(images):
    images_base64 = []
    if not images:
        return HTTPException(status_code=404, detail='No faces found')

    for image in images:
        images_base64.append(base64.b64encode(image))
    return images_base64