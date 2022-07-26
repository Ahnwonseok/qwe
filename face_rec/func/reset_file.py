import os
import shutil
'''
crop_faces 에 생성된 사진을 삭제하고 unrecognized 폴더에 사진을 다시 color_faces로 복사 합니다.

최종 코드에서는 faces폴더에 사진도 초기화 할 수 있게 코드를 수정할 예정
'''

def make_path_list(path): # 경로 만들기
    base_path = path
    path_file = os.listdir(path)
    path_list = [base_path + file for file in path_file]
    return path_list

def DeleteAllFiles():
    try:
        # faces_path = make_path_list('face_rec/images/faces/') # 최종적으로 마무리단계에서 이부분도 주석 해제
        # now_face_path = make_path_list('face_rec/images/now_face/')
        
        crop_path = make_path_list('face_rec/images/crop_faces/')
        crop_now_path = make_path_list('face_rec/images/crop_now_face/')
        unrecognized_path = make_path_list('face_rec/images/unrecognized/')
        try:
            for path in crop_path:
                os.remove(path)
            for path in crop_now_path:
                os.remove(path)
            for path in unrecognized_path:
                os.remove(path)
            # for path in faces_path:
            #     os.remove(path)
            # for path in now_face_path:
            #     os.remove(path)
        except:
            print('PermissionError [WinError 5] 액세스가 거부되었습니다')
            pass
    except:
        pass
    
'''각자 실행할 때'''  
if __name__ == '__main__':
    DeleteAllFiles()