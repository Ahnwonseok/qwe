import cv2
from .trig import trig
import math
import numpy as np

def rotate(imgs,shapes):
    rotated_imgs = []
    for i,shape in enumerate(shapes):
        cos,direction =trig(shape[39],shape[42])
        radians= np.arccos(cos)
        angle = 90 - (radians*180/math.pi)
        (h, w) = imgs[i].shape[:2]
        (cx, cy) = (w // 2, h // 2)
        rotate_matrix = cv2.getRotationMatrix2D((cx, cy), angle*direction, 1.0)
        rotate_img= cv2.warpAffine(np.array(imgs[i]), rotate_matrix, (w, h))
        rotated_imgs.append(rotate_img)
    return rotated_imgs   