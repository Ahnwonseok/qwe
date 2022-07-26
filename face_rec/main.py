from func.comparison import comparison
from func.new_comparison import new_comparison

from func.crop import crop_run
from func.reset_file import DeleteAllFiles
import time


if __name__ == '__main__':
    start = time.time()
    
    crop_run() # 사진 crop
    comparison() # 임베딩 값으로 사진 비교
    
    # new_comparison() # 여러 모델 확인 가능 deepface인증기 포함
    
    DeleteAllFiles() # 사용 가능,불가능한 사진 저장하고 초기화
    print("time :", time.time() - start)