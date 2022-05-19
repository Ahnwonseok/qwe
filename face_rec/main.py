import keras
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import numpy as np
import glob
import dlib
import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()

from model.facenet import Facenet
from function.crop import crop
from function.load_imgs import load_imgs

profile_images_path='./images/profile'
self_image_path= './images/self'
model_path= './model/20180402-114759.pb'

size = (448,448) # 맘대로 수정
input_size= (160,160)# 모델에 삽입되는 사이즈


##-------------------------------------------------Load and crop images --------------------------------------------------------------------##

profile_imgs = load_imgs(profile_images_path,size) # 리스트 반환
self_imgs =load_imgs(self_image_path,size)

profile_faces=[]
for img in profile_imgs:
    detected_faces=crop(img,input_size)
    for detected_face in detected_faces:
        profile_faces.append(detected_face)

self_faces=crop(self_imgs[0],input_size) # 한장만



# ##--------------------------------------------------------prediction--------------------------------------------------------------##
facenet= Facenet(model_path)

print("profile에서 탐지된 얼굴 수 :",len(profile_faces))
print("self에서 탐지된 얼굴 수 :",len(self_faces))

profile_predictions= facenet.get_embeddings(profile_faces)
self_predictions = facenet.get_embeddings(self_faces) 

profile_predictions=np.reshape(profile_predictions,[-1,1,512])
self_predictions=np.reshape(self_predictions,[-1,1,512])


eucledian_dist = []
print("벡터 거리 정보/ 1.1이하는 동일인")
for i in range(len(profile_predictions)):
    for j in range(len(self_predictions)):
        dist=np.linalg.norm(profile_predictions[i]-self_predictions[j])
        eucledian_dist.append(dist)
print(eucledian_dist)
# 느낌 비슷한 연예인 0.8x 


## ----------------------------------- 이미지 체크할 때/ loded_imgs에 profile_imgs 나 self_imgs 를 써서 크로핑 된 이미지를 확인 가능하다 -------------------------------## 
loded_imgs = profile_imgs# select profile_imgs or self_imgs
 
for i in loded_imgs:
    a=crop(i,(160,160))
    a=np.array(a)
    for j in a:
        plt.imshow(j)
        plt.show()


