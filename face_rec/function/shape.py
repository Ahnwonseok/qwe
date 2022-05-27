import dlib
from function.shape_to_np import shape_to_np


def shape(imgs,predictor_path):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)
    shape_list = []
    for img in imgs:
        faces=detector(img)
        for face in faces:
            shape= predictor(img,face)
            shape= shape_to_np(shape)
            shape_list.append(shape)
    return shape_list