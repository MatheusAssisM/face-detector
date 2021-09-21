import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import io

'''
    Get faces from image
'''
def get_faces(image):
    print(image)
    image_gray = _get_resized_gray_image(image)
    return image_gray

'''
    Make image grayscale
'''
def _get_resized_gray_image(image_data):
    image = mpimg.imread(io.BytesIO(image_data), format='jpeg')
    image_resized = _resize_image(image)
    image = cv2.cvtColor(image_resized.copy(), cv2.COLOR_BGR2GRAY)
    _, image_buffer = cv2.imencode('.jpg', image)
    return image_buffer.tobytes()

'''
    Resize the image to a fixed size
'''
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
