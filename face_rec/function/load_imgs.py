import cv2
import glob

def load_imgs(img_path):
    result=[]
    imgs_path_list= [x for x in glob.glob(img_path + '/*.jpg')]

    for img_path in imgs_path_list:
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = cv2.resize(img,fx=1, fy=1,dsize=(0,0),interpolation=cv2.INTER_AREA)
        result.append(img)
    return result # 리스트 형태로 여러장 이미지 반환