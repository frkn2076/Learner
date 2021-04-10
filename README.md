# Learner
**A simple project about machine learning which generates a model that recognizes smile/non-smile images.**

* Dlib's prepared model was used to detect faces in the images (dlib.get_frontal_face_detector()).
* Attached **shape_predictor_68_face_landmarks.dat** model was used to extract landmark positions on the faces.
* Our trainset (**Learner.train**) was created to create our model by train data (**Train-Dataset** folder in project).
* Our testset (**Learner.test**) was created to test our model by test data (**Test-Dataset** folder in project).

## Dataset of Emotion Lab at Karolinska Institutet
* Please refer to https://www.emotionlab.se/kdef/

## Dependencies: 
* pip install cmake
* pip install dlib
* pip install numpy
* pip install Pillow


**PS: Train Set and Test Set was added to project for demonstration.**

