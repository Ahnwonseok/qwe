"""
 얼굴 인증 메인 함수
 실행 시간 : 2.137037992477417
"""
import os
import cv2
import numpy as np
import face_recognition
import shutil
import time
# start = time.time()
# print("time :", time.time() - start)

def get_face_embedding(face):
    '''얼굴을 인식하고 임베딩 값을 구한다.'''
    return face_recognition.face_encodings(face)

def get_face_embedding_dict(dir_path):

    file_list = os.listdir(dir_path)
    embedding_dict = {}
    
    for file in file_list:
        
        img_path = os.path.join(dir_path, file) # 경로를 병합하여 새 경로 생성
        
        face = cv2.imread(img_path)    # 얼굴 영역만 자른 이미지 불러오기
        embedding = get_face_embedding(face)   # 얼굴 영역에서 얼굴 임베딩 벡터를 추출
        
        if len(embedding) > 0:   # crop한 이미지에서 얼굴 영역이 제대로 detect되지 않았을 경우를 대비
            # os.path.splitext(file)[0]에는 이미지파일명에서 확장자를 제거한 이름이 담긴다.
            embedding_dict[os.path.splitext(file)[0]] = embedding[0]
        else:
            # crop한 이미지가 임베딩 값을 구하지 못할 때 원본 사진을 face_recognition.face_encodings한다.
            crop_name = dir_path.split('/')[-2]
            Original_name = crop_name.replace('crop', 'color') # 파일 이름이 바뀌면 이부분도 수정 해야함
            # crop_faces --> color_faces
            # crop_now_faces --> color_now_faces
            face = cv2.imread(f'images/{Original_name}/' + file) # images/color_faces/'IU12.jpg
            embedding = get_face_embedding(face)
            
            embedding_dict[os.path.splitext(file)[0]] = embedding[0]
    return embedding_dict

def comparaion():
    # start = time.time()
    profile_path = 'images/crop_faces/'
    now_face_path = 'images/crop_now_face/'

    profile_photo_embedding_dict = get_face_embedding_dict(profile_path) # 파일 이름과 변환된 임베딩 벡터 딕셔너리
    now_photo_embedding_dict = get_face_embedding_dict(now_face_path)
    
    profile_photo__name = [i for i in profile_photo_embedding_dict.keys()] # 프로필 사진의 이름만 담기
    try:
        now_photo_name = next(iter(now_photo_embedding_dict)) # 현재 사진
    except:
        print('FileNotFoundError : 현재 사진을 넣어주세요')
        pass
    all_img = {} # 전체 프로필 사진

    for i in profile_photo__name:
        embedding = np.linalg.norm(profile_photo_embedding_dict[i]-now_photo_embedding_dict[now_photo_name], ord=2)
        all_img[i] = embedding
    
    allowed_photo = {} # 사용 가능
    disallowed_photo = {} # 사용 불가능
    
    for tup in all_img.items():
        if tup[1] < 0.31: # 임베딩 차 0.3 이하는 동일인 이상은 비동일인
            allowed_photo[tup[0]] = tup[1] # 동일인에 저장
        else:
            disallowed_photo[tup[0]] = tup[1] # 비동일인에 저장
    
    print('등록 하려는 프로필 사진 :\n', all_img, 'count : ', len(all_img))
    print('-------------------')
    print('비동일인 :\n', disallowed_photo)
    print('동일인 :\n', allowed_photo)
    print('-------------------')
    
    if len(all_img) > 0: # 찍은 사진이 1개 이상 있어야한다.
        if len(allowed_photo) >= 1: # 현재와 가장 동일한 사진을 하나 올리면 나머지는 자유
            print('프로필 등록이 완료되었습니다.')
            try:
                # 승인된 프로필 등록 Acceptable_Profiles copy
                color_img_path = 'images/color_faces/'
                accept_path_list = [color_img_path +i[0]+'.jpg' for i in allowed_photo.items()]
                for path in accept_path_list:
                    shutil.copy(path, 'images/Allowed_or_NonAllowed/Acceptable_Profiles/' + path.split('/')[-1])

                # 추가로 승인되지 않은 프로필 등록 Unacceptable_Profiles copy
                path_list = ['images/unrecognized/'+i for i in os.listdir('images/unrecognized/')]
                for path in path_list:
                    shutil.copy(path, 'images/Allowed_or_NonAllowed/Unacceptable_Profiles/' + path.split('/')[-1])
            except:
                pass
        else:
            print(f"현재 본인과 가장 비슷한 사진 len(allowed_photo)개가 부족합니다. 다시 시도하세요")
    else:
        pass
    return


'''각자 실행할 때'''  
if __name__ == '__main__':
    comparaion()