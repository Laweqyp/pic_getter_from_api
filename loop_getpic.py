import time
from src.request_api import get_url_from_api
import os

apikey = input("input apikey ")
num = int(input("count "))
once_num = int(input("single get count "))
# if os.getenv('USER') != '':
#   sys.stdout = open('log.txt', 'w', encoding='utf-8')
programstarttime = time.time()
if not os.path.exists("./pic"):
    os.makedirs("./pic")
if not os.path.exists("./info"):
    os.makedirs("./info")

while num > 0:
    print("[", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "]", "left %d time to get picture" % num)
    singlestarttime = time.time()
    get_url_from_api(apikey, once_num)
    print("单任务结束 用时:", round(time.time() - singlestarttime, 2), 'secs')
    time.sleep(0)
    num -= 1
    print()

print("总任务用时:", round(time.time() - programstarttime, 2), 'secs')
