import unittest


# 사용법: python -m unittest test.TestCase101 또는 초록색 화살표 누르기 ( 개별 )
# unittest.TestCase를 상속받은 클래스를 만든다
class TestCase01(unittest.TestCase):
    def setUp(self):
        """
        테스트 실행 전에 실행 되는 함수
        :return:
        """
        pass

    def tearDown(self) -> None:
        """
        테스트가 종료될 때 마다 실행 되는 함수
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
        # Then - 결과
        pass
