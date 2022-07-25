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

model_name='res10_300x300_ssd_iter_140000.caffemodel'
prototxt_name='deploy.prototxt.txt'

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
                            # print(save + img_name)                                        
                            cv2.imwrite(save + img_name, img[startY:endY,startX:endX])
                            
    unrecog = 'images/unrecognized/'
    if img_name not in os.listdir(save):
            print(img_name.split('.')[-2], '가 아닌 다른 사진을 넣어주세요. --> 얼굴 인식 안됌')
            shutil.copy(c, unrecog+img_name) # 파일 이동
                        


def crop_run():
    try:
        color_img_path = 'images/color_faces/'
        crop_save_path = 'images/crop_faces/'
        color_now_img_path = 'images/color_now_face/'
        crop_now_save_path = 'images/crop_now_face/'
        # 한글 파일은 cv2 오류가 생기기 때문에 랜덤 영문으로 바꿔준다.
        # 나머지 특수문자 숫자는 이상없음
        for c in make_path_list(color_img_path):
            name = Path(c).stem
            extension = os.path.splitext(c)
            
            Korean = re.findall('[가-힣]', name) # 한글 찾기
            # 한글 찾아서 랜덤 영문자로 파일 이름 바꾸기 
            if Korean:
                for i in Korean:
                    name = name.replace(i, f'{random.choice(string.ascii_letters)}')
                file_oldname = c
                file_newname_newfile = color_img_path + name + '.' + extension
                
                os.rename(file_oldname, file_newname_newfile)
            else:
                pass
            if extension == 'png' or 'jpg': # 확장자 확인
                detectAndDisplay(c, crop_save_path)
            else:
                print('Allow png, jpg extensions only')
            
            
        for c in make_path_list(color_now_img_path):
            name = Path(c).stem
            extension = os.path.splitext(c)
            
            Korean = re.findall('[가-힣]', name) # 한글 찾기
            # 한글 찾아서 랜덤 영문자로 파일 이름 바꾸기 
            if Korean:
                for i in Korean:
                    name = name.replace(i, f'{random.choice(string.ascii_letters)}')
                file_oldname = c
                file_newname_newfile = color_img_path + name + '.' + extension
                
                os.rename(file_oldname, file_newname_newfile)
            else:
                pass
            if extension == 'png' or 'jpg': # 확장자 확인
                detectAndDisplay(c, crop_now_save_path)
            else:
                print('Allow png, jpg extensions only')
        
    except:
        print('FileNotFoundError : img')
        return

'''각자 실행할 때'''  
if __name__ == '__main__':
    crop_run()