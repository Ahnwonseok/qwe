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
selfie_image_path= './images/selfie'
model_path= './model/20180402-114759.pb'

size = (448,448) # 맘대로 수정
input_size= (160,160)# 모델에 삽입되는 사이즈


##-------------------------------------------------Load and crop images --------------------------------------------------------------------##

profile_imgs = load_imgs(profile_images_path,size) # 리스트 반환
selfie_imgs =load_imgs(selfie_image_path,size)

profile_faces=[]
for img in profile_imgs:
    detected_faces=crop(img,input_size)
    for detected_face in detected_faces:
        profile_faces.append(detected_face)

selfie_faces=crop(selfie_imgs[0],input_size) # 한장만



# ##--------------------------------------------------------prediction--------------------------------------------------------------##
facenet= Facenet(model_path)

print("profile에서 탐지된 얼굴 수 :",len(profile_faces))
print("selfie에서 탐지된 얼굴 수 :",len(selfie_faces))

profile_predictions= facenet.get_embeddings(profile_faces)
selfie_predictions = facenet.get_embeddings(selfie_faces) 

profile_predictions=np.reshape(profile_predictions,[-1,1,512])
selfie_predictions=np.reshape(selfie_predictions,[-1,1,512])


eucledian_dist = []
print("벡터 거리 정보/ 0.96 이하는 동일인")
for i in range(len(profile_predictions)):
    for j in range(len(selfie_predictions)):
        dist=np.linalg.norm(profile_predictions[i]-selfie_predictions[j])
        eucledian_dist.append(dist)
print(eucledian_dist)
# 느낌 비슷한 연예인은 간혹 0.8x 까지 나오고 본인은 보통 심하면 0.9xx 까지 나온다
# 간혹 탐지가 안 될 경우 탐지된 얼굴 개수가 0이 나온다 그러면 사진을 바꾸거나 프로필 사진을 추가로 넣어줘야 한다 gpu 기반이 아니라 가끔 빠뜨리는 경우가 있다. 하지만 크게 잘 찍은 사진은 어지간하면 다 탐지한다


## ----------------------------------- 이미지 체크할 때/ loded_imgs에 profile_imgs 나 selfie_imgs 를 써서 크로핑 된 이미지를 확인 가능하다 -------------------------------## 
loded_imgs = profile_imgs# select profile_imgs or selfie_imgs
 
for i in loded_imgs:
    a=crop(i,(160,160))
    a=np.array(a)
    for j in a:
        plt.imshow(j)
        plt.show()


