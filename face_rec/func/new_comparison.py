"""
 얼굴 인증 메인 함수
 실행 시간 : 2.137037992477417
"""
import os
import numpy as np
from deepface import DeepFace
import time
import cv2
import shutil
import glob
import pandas as pd
# start = time.time()
# print("time :", time.time() - start)
 
def new_comparison():
    profile_dir = 'face_rec/images/now_face/' #현재 프로필 디렉토리
    profile_name = os.listdir(profile_dir) #현재 프로필 이름

    img_list = glob.glob('face_rec/images/faces/*.jpg') #비교하는 사진 리스트
    unrecog = 'face_rec/images/unrecognized/' #얼굴탐지 못한 사진이 갈 주소
    save = 'face_rec/images/crop_faces/' #얼굴탐지 된 사진이 갈 주소
    #모델변경 가능
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]

    resp=[]
    for img in img_list:  
        img_name = img.split("\\")[-1]
        try:                            #img_path : profile 사진   /  img2_path = 비교하는 사진
            resp.append(DeepFace.verify(img1_path=profile_dir+profile_name[0], img2_path=img, model_name=models[2]))
            #인식을 잘하면 crop_faces로 보냄
            shutil.copy(img, save+img_name) 

        #얼굴 인식을 못하면 unrecog로 보냄                
        except: 
            shutil.copy(img, unrecog+img_name) 

    df=pd.DataFrame(resp)
    print(df)

'''각자 실행할 때'''  
if __name__ == '__main__':
    new_comparison()