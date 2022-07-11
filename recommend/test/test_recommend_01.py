import unittest
import inspect


# 사용법: python -m unittest test.TestCase101 또는 초록색 화살표 누르기 ( 개별 )
# unittest.TestCase를 상속받은 클래스를 만든다
class TestCase01(unittest.TestCase):
    """1자리 숫자 연산을 확인한다"""

    def setUp(self):
        """
        테스트 실행 전 전체 테스에 적용 해야하는 세팅 해야 하는 함수
        :return:
        """
        pass

    def test_main_is_run(self):
        """
        테스트 함수를 적는 함수
            * 함수 명은 test_로 시작해야 한다
            * 함수 명은 테스트하는 이유 를 적는 것이 바람직
        :return: None
        """
        # 함수 명은 test_로 시작 해야 한다
        # Given - 테스트 준비

        # When - 실행
        a = main()
        # Then - 결과
        self.assertEqual(a, 10)


# unittest를 실행
if __name__ == '__main__':
    unittest.main()
