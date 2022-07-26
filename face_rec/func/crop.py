'''
find face and crop, grayscale

실행 시간 : 0.5425937175750732
'''
import os
import cv2
import numpy as np
import face_recognition
import dlib
import shutil
import time
import re
import random
import string
from pathlib import Path
# start = time.time()
# print("time :", time.time() - start)


def make_path_list(path): # 경로 만들기
    base_path = path
    path_file = os.listdir(path)
    path_list = [base_path + file for file in path_file]
    return path_list

model_name='face_rec/res10_300x300_ssd_iter_140000.caffemodel'
prototxt_name='face_rec/deploy.prototxt.txt'

def detectAndDisplay(c,save):
    # 원본 사진을 face_recognition.face_encodings 를 활용해
    # crop과 encoding을 할 수 있지만 시간이 오래걸리기 때문에
    # 크롭하고 인코딩값을 구한다.
    img = cv2.imread(c)
    (height, width) = img.shape[:2]
    model=cv2.dnn.readNetFromCaffe(prototxt_name,model_name)
    blob=cv2.dnn.blobFromImage(cv2.resize(img,(300,300)),1.0, (300,300),(104.0,177.0,123.0))
    
    model.setInput(blob)
    
    detections=model.forward()
    for i in range(0, detections.shape[2]):
    
        confidence = detections[0, 0, i, 2]
        min_confidence=0.9
        img_name = c.split('/')[-1]
            
        if confidence > min_confidence:
              
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype("int")
            
            if height > endY and width > endX : #예외처리   
                cv2.imwrite(save + img_name, img[startY:endY,startX:endX])
                            
    unrecog = 'face_rec/images/unrecognized/'
    if img_name not in os.listdir(save):
            print(img_name.split('.')[-2], '가 아닌 다른 사진을 넣어주세요. --> 얼굴 인식 안됌')
            shutil.copy(c, unrecog+img_name) # 파일 복사
                        


def crop_run():
    img_path = 'face_rec/images/faces/'
    now_img_path = 'face_rec/images/now_face/'
    crop_save_path = 'face_rec/images/crop_faces/'
    crop_now_save_path = 'face_rec/images/crop_now_face/'
    
    for e in os.listdir(img_path) + os.listdir(now_img_path):
        extension = e.split('.')[-1]
        if extension == 'png' or 'jpg': # 확장자 확인
            pass
        else:
            print('Allow png, jpg extensions only')
    
    
    # 한글 파일은 cv2 오류가 생기기 때문에 랜덤 영문으로 바꿔준다.
    # 나머지 특수문자 숫자는 이상없음
    for c in make_path_list(img_path):
        name = Path(c).stem
        extension = c.split('.')[-1]
        
        # 영어, 숫자, 특수문자 외에 문자 변경
        Unacceptable_characters = re.findall('[^A-Za-z0-9]', name)
        for i in re.findall('^[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', name):
            Unacceptable_characters.append(i)
        
        # 한글 찾아서 랜덤 영문자로 파일 이름 바꾸기 
        if Unacceptable_characters:
            for i in Unacceptable_characters:
                name = name.replace(i, f'{random.choice(string.ascii_letters)}')
                
            oldfile_path = c
            newfile_path = img_path + name + '.' + extension
            os.rename(oldfile_path, newfile_path)

    
            
            
    for c in make_path_list(now_img_path):
        name = Path(c).stem
        extension = c.split('.')[-1]
        
        # 영어, 숫자, 특수문자 외에 문자 변경
        Unacceptable_characters = re.findall('[^A-Za-z0-9]', name)
        for i in re.findall('^[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', name):
            Unacceptable_characters.append(i)
        
        # 한글 찾아서 랜덤 영문자로 파일 이름 바꾸기 
        if Unacceptable_characters:
            for i in Unacceptable_characters:
                name = name.replace(i, f'{random.choice(string.ascii_letters)}')
                
            oldfile_path = c
            newfile_path = img_path + name + '.' + extension
            os.rename(oldfile_path, newfile_path)

    
    path_list = make_path_list(img_path)         
    now_path_list = make_path_list(now_img_path)

    # 위 반복문이 끝나고 바뀐 path를 가지고 detectAndDisplay
    for p in path_list:
        detectAndDisplay(p, crop_save_path)
        
    for p in now_path_list:
        detectAndDisplay(p, crop_now_save_path)
    
            
'''각자 실행할 때'''  
if __name__ == '__main__':
    crop_run()