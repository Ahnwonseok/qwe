import unittest
import sys
sys.path.append('.') # working dir --> face_rec
import os
import re

from func.crop import detectAndDisplay

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
        It_should_be_zero = 0
        color_img_path = len(os.listdir('images/color_faces/'))
        color_now_img_path = len(os.listdir('images/color_now_face/'))
        if color_img_path == 0:
            It_should_be_zero += 1
        if color_now_img_path == 0:
            It_should_be_zero += 1
            
        self.assertFalse(It_should_be_zero , 'done')

    # def test_File_name_not_changed():
        
            
if __name__ == '__main__':
     unittest.main()