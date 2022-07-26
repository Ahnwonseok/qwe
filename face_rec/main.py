from func.comparison import comparison
from func.crop import crop_run
from func.reset_file import DeleteAllFiles
import time


if __name__ == '__main__':
    crop_run()
    start = time.time()
    comparison()
    print("time :", time.time() - start)
    DeleteAllFiles()