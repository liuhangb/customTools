# import os
# import time
# from datetime import datetime
#
# cmd = "adb shell dumpsys meminfo com.mt.mtxx.mtxx"
# while 1:
#     os.system(cmd)
#     print(datetime.now())
#     time.sleep(1)


import os

base = '/Users/liuhang/downloads/Meitu-9.9.6.1-20230825112706-setup64-setup64Release-daily/lib/arm64-v8a'
for filename in os.listdir(base):
    print(filename)
