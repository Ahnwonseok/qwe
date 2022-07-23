import os
import shutil
'''
crop_gray_faces 에 생성된 사진을 삭제하고 unrecognized 폴더에 사진을 다시 color_faces로 옮깁니다.
'''

def make_path_list(path): # 경로 만들기
    base_path = path
    path_file = os.listdir(path)
    path_list = [base_path + file for file in path_file]
    return path_list

def DeleteAllFiles():
    try:
        crop_gray_path = make_path_list('images/crop_gray_faces/')
        crop_gray_now_path = make_path_list('images/crop_gray_now_face/')
        unrecognized_path = make_path_list('images/unrecognized/')
        try:
            for path in crop_gray_path:
                os.remove(path)
            for path in crop_gray_now_path:
                os.remove(path)
            for path in unrecognized_path:
                destination = 'images/color_faces/' + path.split('/')[-1] # 이동할 경로
                shutil.move(path, destination)
        except:
            print('[WinError 5] 액세스가 거부되었습니다')
            raise PermissionError
    except:
        pass

if __name__ == '__main__':
    DeleteAllFiles()


