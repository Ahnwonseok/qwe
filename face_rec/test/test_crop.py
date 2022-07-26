import sys
sys.path.append('.') # working dir --> Sinor_AI
import unittest
import os
import re

from face_rec.func.crop import detectAndDisplay

# 사용법: python -m unittest test.TestCase101 또는 초록색 화살표 누르기 ( 개별 )
# unittest.TestCase를 상속받은 클래스를 만든다
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('start')
        
    def tearDown(self) -> None:
        print('end')

    def test_more_than_one_image(self):
        """
        테스트 함수를 적는 함수
            * 함수 명은 test_로 시작해야 한다
            * 함수 명은 테스트하는 이유 를 적는 것이 바람직
        :return: None
        """
        # 함수 명은 test_로 시작 해야 한다
        # Given - 테스트 준비
        
        faces_img_path = len(os.listdir('face_rec/images/faces/'))
        now_face_img_path = len(os.listdir('face_rec/images/now_face/'))
        
        It_should_be_zero = 0
        '''프로필로 사용할 사진이 폴더에 1개 이상 있어야한다.'''
        if faces_img_path == 0: # 사진이 없을 때 It_should_be_zero에 1추가
            It_should_be_zero += 1
            
        '''현재 사진으로 사용할 사진이 폴더에 1개 이상 있어야한다.'''
        if now_face_img_path == 0:
            It_should_be_zero += 1
            
        '''It_should_be_zero 가 1 이상이면 폴더에 사진이 없음을 의미'''
        self.assertFalse(It_should_be_zero , 'done')

            
if __name__ == '__main__':
     unittest.main()