import dlib
import os
import sys
from PIL import Image
face_detector = dlib.get_frontal_face_detector()
landmark_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#if images are not scaled, scale them.
# image = Image.open(img_path)
# new_image = image.resize((400, 400))

def print_landmarks_to_file(img, faces, file, isSmile):
  # count of faces in the image
  face_count = len(faces)
  if face_count == 0:
    print('No face was found in the image')
    sys.exit()

  if face_count > 1:
    print('More than one face was found in the image')
    sys.exit()

  face = faces[0]

  # detect facial landmarks
  landmarks = landmark_detector(img, face)
  
  # 1 represents smile class, -1 represents non-smile class.
  file.write("1 " if isSmile else "-1 ")
  
  for n in range(0, 68):
    # x, y coordinates divided by 1000 for converting values 0-1 range.
    x = landmarks.part(n).x / 1000
    y = landmarks.part(n).y / 1000
    file.write(f'{n*2+1}:{x} ')
    file.write(f'{n*2+2}:{y} ')
  
  file.write("\n")


def print_landmarks_to_file_by_paths(file, paths, isSmile):
  for path in paths:
    #read image with dlib
    img = dlib.load_rgb_image(path)
    #detect faces in the image
    faces = face_detector(img, 1)
    #print landmarks to file
    print_landmarks_to_file(img, faces, file, isSmile)

def get_paths(folder_name):
  files_names = os.listdir(folder_name)
  paths_of_files = list(map(lambda file_name: os.path.join(folder_name, file_name), files_names))
  return paths_of_files

train_nonsmile_paths = get_paths(os.path.join('Train-Dataset', 'non-smile'))
train_smile_paths = get_paths(os.path.join('Train-Dataset', 'smile'))
test_nonsmile_paths = get_paths(os.path.join('Test-Dataset', 'non-smile'))
test_smile_paths = get_paths(os.path.join('Test-Dataset', 'non-smile'))

## TRAIN DATA OPERATIONS ##########################################

# open a file to print landmarks
my_train_file = open("Learner.train","w")

# Extracting landmarks of smile images
print_landmarks_to_file_by_paths(my_train_file, train_smile_paths, True)

# Extracting landmarks of non-smile images
print_landmarks_to_file_by_paths(my_train_file, train_nonsmile_paths, False)

my_train_file.close()


## TEST DATA OPERATIONS ###########################################

# open a file to print landmarks
my_test_file = open("Learner.test","w")

# Extracting landmarks of smile images
print_landmarks_to_file_by_paths(my_test_file, test_smile_paths, True)

# Extracting landmarks of non-smile images
print_landmarks_to_file_by_paths(my_test_file, test_nonsmile_paths, False)

my_test_file.close()

