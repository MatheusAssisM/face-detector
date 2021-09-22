import cv2
import matplotlib.image as mpimg
import io
import dlib

# Get faces from image


def get_faces(image):
    face_detector = _build_face_detector()
    image_resized = _get_resized_image(image)
    marked_image = _build_rectangle_on_image(image_resized, face_detector)
    image_buffered = _get_buffered_image(marked_image)
    return image_buffered

# Make image grayscale
def _get_resized_image(image_data):
    image = mpimg.imread(io.BytesIO(image_data), format='jpeg')
    # image_resized = _resize_image(image)
    image_rgb = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    return image_rgb


# Resize the image to a fixed size
def _resize_image(image, scale_percent=50):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image_resized = cv2.resize(
        image.copy(),
        dim,
        interpolation=cv2.INTER_AREA
    )
    return image_resized

# Get the face predictor and the classifier
def _build_face_detector():
    _classifier_68_path = './app/utils/classifiers/shape_predictor_68_face_landmarks.dat'
    dlib.shape_predictor(_classifier_68_path)
    face_detector = dlib.get_frontal_face_detector()
    return face_detector

# Build the rectangle around the face
def _build_rectangle_on_image(image, face_detector):
    faces = face_detector(image, 1)
    if not faces:
        return None

    for _, d in enumerate(faces):
        cv2.rectangle(
            image, 
            (d.left(), d.top()), 
            (d.right(), d.bottom()), 
            (255, 0, 0), 
            2
        )
    return image

# Get buffered image
def _get_buffered_image(image):
    _, image_buffer = cv2.imencode('.jpg', image)
    return image_buffer.tobytes()