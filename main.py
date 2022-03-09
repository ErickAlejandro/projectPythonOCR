import cv2
import pytesseract as pt

img = cv2.imread('/home/foranito/learningPython/projectPython/cedulas_transformadas/C27.png')
# img = str(img)
# print(img)
# Adding custom options
custom_config = r'--oem 3 --psm 6'
img_t = pt.image_to_string(img, config=custom_config)
print(str(img_t))

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)