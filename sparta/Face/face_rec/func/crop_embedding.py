'''
find face and crop and embedding

실행 시간 : 0.5425937175750732
''' 
import cv2
import numpy as np
import face_recognition
import time
import sys 
import mediapipe as mp
import math
import requests
import matplotlib.pyplot as plt
# start = time.time()
# print("time :", time.time() - start)

'''얼굴 이미지를 임베딩값으로 변환'''
def get_face_embedding_dict(numbering, url, img): # numbering = img번호, url = 사진주소, img = 이미지 자체

    embedding = face_recognition.face_encodings(img)   # 얼굴 영역에서 얼굴 임베딩 벡터를 추출
    
    if len(embedding) > 0:   # crop한 이미지에서 얼굴 영역이 제대로 detect되지 않았을 경우를 대비
        '''crop한 사진에서 임베딩값을 구한경우 통과'''
        return embedding[0] # 임베딩 값 리턴
    else:
        '''crop한 이미지가 임베딩 값을 구하지 못할 때 원본 사진으로 임베딩값을 구한다.'''
        try:                                                                
            image_nparray = np.asarray(bytearray(requests.get(url,timeout=3).content), dtype=np.uint8)
            image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

        except : image = None #url에서 이미지를 못불러오면 image에 None값을 삽입

        embedding = face_recognition.face_encodings(image)

        '''원본 사진을 인식한 경우'''
        if len(embedding) > 0: 
            return embedding[0] # 임베딩 값 리턴

        else: 
            '''원본 사진마저 인식을 못하는 경우'''
            # 나중에 다른모델로 detection할 수 있음
            
            if numbering == 0: # 셀카를 인식 못하면 프로그램 종료
                sys.exit('셀카를 인식할 수 없습니다')

            else : #셀카가 아니면 계속 진행     
                print(url, '가 아닌 다른 사진을 넣어주세요. --> 얼굴 인식 안됌') 

            return None #원본사진마저 인식을 못하는 경우 None을 리턴
       
    
model_name='res10_300x300_ssd_iter_140000.caffemodel'
prototxt_name='deploy.prototxt.txt'

def detectAndDisplay(img):
    # 원본 사진을 face_recognition.face_encodings 를 활용해
    # crop과 encoding을 할 수 있지만 시간이 오래걸리기 때문에
    # 크롭하고 인코딩값을 구한다.
    
    (height, width) = img.shape[:2]
    model=cv2.dnn.readNetFromCaffe(prototxt_name,model_name)
    blob=cv2.dnn.blobFromImage(cv2.resize(img,(300,300)),1.0, (300,300),(104.0,177.0,123.0))
    
    model.setInput(blob)
    
    detections=model.forward()

    '''crop 과정'''
    min_confidence=0.9
    result_img = None

    for i in range(0, detections.shape[2]):
        
        confidence = detections[0, 0, i, 2]
        
        if confidence > min_confidence:
              
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype("int")
            
            if height > endY and width > endX and startX > 0 and startY > 0: #얼굴탐지를 이미지 내에서 해야함
                result_img = img[startY:endY,startX:endX]  
                min_confidence = confidence  #얼굴인식 최소 확률을 현재 확률로 정함            

    '''crop을 했을 경우''' 
    if result_img is not None:
        # plt.imshow(result_img)
        # plt.show()
        return result_img
    
    else:    
        '''crop 하지 못하는경우'''
        return []

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
                                static_image_mode=True,
                                max_num_faces=1,
                                refine_landmarks=True,
                                min_detection_confidence=0.5)

'''얼굴 이미지의 수평을 맞춘다.'''
def rotate_img(image):
    result = face_mesh.process(image) #얼굴을 탐지한다.
    height, width = image.shape[:2]
    
    try : #얼굴 탐지가 잘 됐을 경우
        for facial_landmarks in result.multi_face_landmarks:
            x_min = width
            x_max = 0
            y_min = height
            y_max = 0

            for i in range(0, 468): # 랜드마크 (x, y) 0부터 468      
                pt = facial_landmarks.landmark[i]
                x = int(pt.x * width)
                y = int(pt.y * height)
                
                if x < x_min:
                    x_min = x
                if x > x_max:
                    x_max = x
                if y < y_min:
                    y_min = y
                if y > y_max:
                    y_max = y  
                    
            mid_forehead_X = facial_landmarks.landmark[9].x # 중앙 미간 x
            mid_forehead_Y = facial_landmarks.landmark[9].y # 중앙 미간 y
            mid_chin_X = facial_landmarks.landmark[152].x # 중앙 턱 x
            mid_chin_Y = facial_landmarks.landmark[152].y # 중앙 턱 y
            
            '''얼굴 수평 이동'''
            tan_theta = (mid_chin_X - mid_forehead_X)/(mid_chin_Y - mid_forehead_Y)
            theta = np.arctan(tan_theta)
            rotate_angle = theta *180/math.pi
            rot_mat = cv2.getRotationMatrix2D((height, width), -rotate_angle, 1.0)
            image  = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR, borderValue=(255,255,255))
        
            rotate_image = image.copy()             
            # cv2.imshow('a',rotate_image)
            # cv2.waitKey(0)
        return rotate_image #수평을 맞춘 이미지 반환

    #얼굴 탐지를 못하면 기존의 이미지를 반환한다.    
    except: return image

#얼굴 이미지를 수평으로 반환하는 함수
def conversion(image):
    '''이미지가 너무 크면 오류남'''
    if image.shape[0] > 1500 or image.shape[1] > 1500: # 너비 높이 1500 이상이면 보간법으로 이미지 축소 
        image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4, interpolation=cv2.INTER_LINEAR)
    
    original_image = image.copy()
    
    # rotate
    rotate_image = rotate_img(original_image)

    return rotate_image

def img_embedding(path): #path는 main.py에 있는 txt디렉토리
    faces_url_list = [] # url리스트
    '''faces.txt 에서 url리스트를 가져온다''' # faces.txt의 url리스트가 0이상 없으면 종료
    with open(path, "r") as f:
        data = f.readlines() #data는 txt파일에 있는 url주소 리스트
    
        if len(data) <= 1: #이미지가 한 장 이하이면 프로그램 종료
            sys.exit('이미지가 없습니다.')

        for num, line in enumerate(data):
            extension = line.split('.')[-1].strip() #확장자

            if extension in ['jpg','png','jpeg','jfif']: # 올바른 확장자인지 판별
                faces_url_list.append(line.strip())  #올바른 확장자일 때만 이미지 주소추가 수정

            else:
                print('Allow png, jpg, jpeg, jfif extensions only')
                
                if num == 0: #만약 '셀카'의 확장자가 이상하면 프로그램 종료
                    sys.exit(f'셀카의 확장자가 {extension} 입니다.')
                    
                      
    img_dict = {} # {0:[array], 1:[array], 2:[array], 3:[array], 4:[array]} value = 임베딩값
    '''위 img_dict 딕셔너리를 위해 주소가 아닌 "0", "1", "2"... numbering 으로 바꿈'''
    for numbering, url in enumerate(faces_url_list):

        try:
            '''url로 이미지 받아오기'''
            image_nparray = np.asarray(bytearray(requests.get(url,timeout=3).content), dtype=np.uint8)
            image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

        except:
            #셀카 이미지를 받아올 수 없으면 프로그램 종료
            if numbering == 0:
                sys.exit('셀카 이미지를 받아올 수 없습니다.')

            print('해당 url 이미지를 불러올 수 없음')
            image = None

        '''image를 잘 받았을 때 crop하기'''
        if image is not None:

            crop_img = detectAndDisplay(image) #인자값: url에서 받은 이미지       

            '''crop을 실패했을 때 원본 이미지로 임베딩 값 구하기'''
            if len(crop_img) == 0: # crop_img = 위 리턴값을 []로 했기 때문에 리스트 내용은 0
                image = conversion(image) # image 얼굴의 수평을 맞춘다.
                original_embedded = get_face_embedding_dict(numbering, url, image) # 숫자이름, 이미지 주소, 원본 이미지
            
                if original_embedded is not None : # 임베딩 값을 구했으면 딕셔너리에 삽입                         
                    img_dict[numbering] = original_embedded # key = 숫자이름, value = 임베딩값          
            
            else : 
                '''#crop이 성공했을 때 임베딩 값 구하기'''    
                crop_img = conversion(crop_img) # crop_img 얼굴의 수평을 맞춘다.                          
                crop_embedded = get_face_embedding_dict(numbering, url, crop_img) # 숫자이름, 이미지 주소, 원본 이미지
             
                if crop_embedded is not None: # 임베딩 값이 구했으면 딕셔너리에 삽입                   
                    img_dict[numbering] = crop_embedded # key = 숫자이름, value = 임베딩값 


    '''만약 프로필 사진을 한 장 이하로 인식을 했다면'''    
    if len(img_dict) <= 1:
        sys.exit('인식할 수 있는 프로필 사진이 없습니다')

    return img_dict # 딕셔너리 리턴 / key: 숫자이름, value: 임베딩값