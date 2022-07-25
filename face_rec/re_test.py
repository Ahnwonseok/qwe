import re
import os

color_img_path = os.listdir('images/color_faces/')
for i in color_img_path:
    It_should_be_zero = 0
    for name in color_img_path: 
        name = re.findall('[^A-Za-z0-9가-힣]', i)
        # name = re.findall('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', name)
        print(name)
        # if 0 > len(re.findall('[^A-Za-z0-9가-힣]', i)): #  or 0 < len(re.findall('^[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]')):
        #     It_should_be_zero += 1
