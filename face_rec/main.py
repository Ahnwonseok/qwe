from func.comparison import comparison
from func.crop import crop_run
from func.reset_file import DeleteAllFiles
import time


if __name__ == '__main__':
    start = time.time()
    crop_run()
    comparison()
    DeleteAllFiles()
    print("time :", time.time() - start)