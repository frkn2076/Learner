import dlib
from PIL import Image
face_detector = dlib.get_frontal_face_detector()
landmark_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#image path
img_path = "***.jpg"

image = Image.open(img_path)

#if images are not scaled, scale them.
# new_image = image.resize((400, 400))

# new_image.show()

#read image with dlib
img = dlib.load_rgb_image(img_path)

#detect faces in the image
faces = face_detector(img, 1)

landmark_tuple = []
for k, d in enumerate(faces):
   # detect landmarks
   landmarks = landmark_detector(img, d)
   for n in range(0, 68):
      x = landmarks.part(n).x
      y = landmarks.part(n).y
      print("order:", n, "=> x:", x, " y:", y)