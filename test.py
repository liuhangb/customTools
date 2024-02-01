# crashDeviceNum = [4462, 6033, 9180, 10684, 11459, 11320, 12281]
# crashDeviceRatio = [0.3045, 0.3444, 0.3699, 0.3683, 0.3748, 0.3738, 0.3510]
# for i in range(len(crashDeviceNum)):
#     value = crashDeviceNum[i] / crashDeviceRatio[i] * 100
#     print("", value)

#计算是否存在崩溃未上报事件重复上报问题
# import csv
#
# unReportAnr = csv.reader(open("/Users/liuhang/downloads/新查询3_15594633_5.csv"))
# anrCrash = csv.reader(open("/Users/liuhang/downloads/潮自拍_6485544_119.csv"))
# unReportAnrGid = set([])
# for row in unReportAnr:
#     if (row[0].isnumeric() == False): continue
#     unReportAnrGid.add(row[0])
#
# print(unReportAnrGid)
#
# for row in anrCrash:
#     if (row[0].isnumeric() == False): continue
#     if(row[0] in unReportAnrGid): print(row[0])

import os
import time

cmd = "curl 'https://form-preview-api.eqxiu.com/lp/valid?code=3s9x90F2&ssid=undefined' \
  -H 'authority: form-preview-api.eqxiu.com' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' \
  -H 'origin: https://forms.ebdan.net' \
  -H 'referer: https://forms.ebdan.net/ls/3s9x90Fl?boostCode=H5y4yh31&share_level=1&from_user=20230814eba63df1&from_id=fd69d86e-6&share_time=1692093574685&submitAgain=true' \
  -H 'sec-ch-ua: \"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-ch-ua-platform-version: \"13.3.0\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36' \
  --compressed"

for i in range(1):
    os.system(cmd)
    time.sleep(2)