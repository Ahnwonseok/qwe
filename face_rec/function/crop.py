import dlib
import numpy as np
import cv2

def crop(image,input_size):# 이미지 하나, 모델에 들어갈 사이즈
    imgs=[]
    detector = dlib.get_frontal_face_detector()
    faces = detector(image)
    for face in faces:
        face_img=image[face.top():face.bottom(), face.left():face.right()]
        face_img=cv2.resize(face_img,dsize=input_size)
        face_input=face_img.copy().reshape((input_size[1], input_size[0], 3)).astype(np.float32)/255.
        imgs.append(face_input)
    return imgs# 얼굴 여러개