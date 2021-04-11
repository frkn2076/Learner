# Learner
**A simple project about machine learning which generates a model that recognizes smile/non-smile images.**

* Dlib's prepared model was used to detect faces in the images (dlib.get_frontal_face_detector()).
* Attached **shape_predictor_68_face_landmarks.dat** model was used to extract landmark positions on the faces.
* Our trainset (**Learner.train**) was created to create our model by train data (**Train-Dataset** folder in project).
* Our testset (**Learner.test**) was created to test our model by test data (**Test-Dataset** folder in project).
<br>
<h1 align="center">68 Facial Landmarks</h1> 
<p align="center">
  <img src="https://github.com/frkn2076/Learner/blob/main/facial_landmarks_68markup.jpg" width="600" height="500">
</p>
<br>

## Cohn Kanade Dataset
* Please refer to https://www.kaggle.com/c/bda-2020-facial-expressions/data for dataset
  * pip install kaggle
  * kaggle datasets download -d xwdcrab/ckplus-ocface



## Dependencies: 
* pip install cmake
* pip install dlib
* pip install numpy
* pip install Pillow

<br>
**PS: Train Set and Test Set was added to project for demonstration.**

