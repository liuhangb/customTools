import os
import re
import json
import time



def getCmd(gid, startTime, endTime):
    return "curl 'https://shenji.tatstm.com/api/behaviour/track/query' \
      -H 'Accept: application/json, text/plain, */*' \
      -H 'Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' \
      -H 'Connection: keep-alive' \
      -H 'Content-Type: application/json' \
      -H 'Cookie: _sm=18953b81522c02-0c744692b7ba03-1c525634-1296000-18953b8152322ff; meitustat={%22wgid%22:%2218953b81522c02-0c744692b7ba03-1c525634-1296000-18953b8152322ff%22}; sso_user=\"A/IowePAUxo+Q3beJiqz7VVLZ3dkDUQqT8PKrQDp2TUP4Z4d9cmWJPtEQFwUp/9uWGf+m4Vtky8ADkDE8egnZzG3JXnMe/Mcy4kQs2dZ7V72lZZVcT/UCdyKmzJjQkRmqC7y87/AnFUUR2QjH0Q3xA3fC0gWlhV2xqKHf2unJx0dyTF9kO+kV9gQ/t1On7fH2Ix4J8YuWRwOpzA0hrFgLi7m+17jMgN1Ff8UiUrOOxUhXrKXODzdPMfZJWVKcLC3WSI6opKDN2NcGTaP6M2qqNuwqHkwddgeOB7FyoyQ8OYIoFsYC54REgeoAGyENRx7xLmBHny4jUwUtxnLDg/jTquIsMOORVgJU2nMBjep0i/d7hdsKFDDCUMTO9SRvF8HAlZz+3pYpgJ/ztZHjsl3DvV4V2JmSuRp4oNH+H99eda00zupnY99GczmHoexHO4F8DgaggHoJdxSVR9cOaUzxb5zRb0j/imMTn/M8gBxb08iTZeHXBYgQe+i104JPzqCNLdwkUN3kk++C0mgE37Psd448Gd1Sa2S2MYBI+beBE11pz43qxaiBxNt5RsEdbLIzDPLg1Zx5genZh1rODW+uw==\"; sso_access_token=\"A/IowePAUxo+Q3beJiqz7VY5Mv4rMtPl0MhvohuEzAKZMebTqCuVPoc25xIICgSM9fSTDkMbpGAVJPO33d4aYgTo2f1T8ul+9aMinmZ4Q+fiHxv0kVt2rMrJYbvA7IwNmlG71T+mqXF/HgED25ykjA==\"; JSESSIONID=A1192D4387C39CB51C2B9319B2AB238D' \
      -H 'Origin: https://shenji.tatstm.com' \
      -H 'Referer: https://shenji.tatstm.com/user/behavior?appName=whee&appType=1&flagType=gid&flagValue=2941852611&start=1706284800000&end=1706371199999&session_id=NmvFGj9gnc3THPjkOKvySWhym6RJ56Yo&utm_source=tianwen&openParams=0&fields=gid%2Cevent_id%2C%E4%BA%8B%E4%BB%B6%E5%90%8D%E7%A7%B0%2Ctime%2Capp_version%2Cdevice_model%2Cchannel%2Cparams&useCache=1&showDelayEvent=1&showSystemEvent=1' \
      -H 'Sec-Fetch-Dest: empty' \
      -H 'Sec-Fetch-Mode: cors' \
      -H 'Sec-Fetch-Site: same-origin' \
      -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
      -H 'X-Dataworks-OwnerUid: 6398' \
      -H 'X-Dataworks-ProjectIds: 117' \
      -H 'X-Dataworks-RoleId: 6649' \
      -H 'X-Dataworks-RoleType: 0' \
      -H 'appType: 1' \
      -H 'curReqId: 65bb0fee7c34911d20da8d4b' \
      -H 'preReqId: 65bb0fe37c34911d20da8d4a' \
      -H 'projectId: 117' \
      -H 'sec-ch-ua: \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"' \
      -H 'sec-ch-ua-mobile: ?0' \
      -H 'sec-ch-ua-platform: \"macOS\"' \
      --data-raw '{\"flagType\":\"gid\",\"flagValue\":\"" + gid + "\",\"date\":{\"start\":" + startTime + ",\"end\":" + \
           endTime + "},\"useCache\":1,\"showSystemEvent\":1,\"showDelayEvent\":1,\"pageNum\":0,\"moduleId\":\"\",\"pageSize\":20,\"fields\":\"gid,event_id,事件名称,time,app_version,device_model,channel,params\",\"where\":{\"and\":[{\"id\":20211916,\"fieldDimension\":1,\"function\":\"=\",\"args\":[\"whee_pages_expo\"],\"fieldName\":\"event_id\"}]}}' \
      --compressed"


crashListCmd = "curl 'https://lingwen.tatstm.com/api/server/crash/logList' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Cookie: sso_user=A/IowePAUxo+Q3beJiqz7VVLZ3dkDUQqT8PKrQDp2TUP4Z4d9cmWJPtEQFwUp/9uWGf+m4Vtky8ADkDE8egnZzG3JXnMe/Mcy4kQs2dZ7V72lZZVcT/UCdyKmzJjQkRmqC7y87/AnFUUR2QjH0Q3xA3fC0gWlhV2xqKHf2unJx0dyTF9kO+kV9gQ/t1On7fH2Ix4J8YuWRwOpzA0hrFgLi7m+17jMgN1Ff8UiUrOOxUhXrKXODzdPMfZJWVKcLC3WSI6opKDN2NcGTaP6M2qqNuwqHkwddgeOB7FyoyQ8OYIoFsYC54REgeoAGyENRx7xLmBHny4jUwUtxnLDg/jTg2OqxMnhlk4xURhOexIVgLs0KqYN54GI5ILO//Sk+KaNc3PcXdbA+B5XZo9flNi8nYubWII2lGQr0lAkNCiDdek8G7en6EIng1HevLTVFT+oRnTbiUL1p9O7gOdpeVpFUp1scliSJbfz54pjtgdmosXP9bNj6sF0UgVNNyypS12XqhNLy3EOgrWuTpwu13wuf9Sv9s4F9Mzgu7jQ3rxs/IYpZFMdar+LiIqIxIRHHaZxhGCHT7KCGM1vP8hC9ljp1fCvRKPfFzbtkiKJXv4eoW9DDfTKbZ1EU5zi0+skm310BXJQcmyawxcgwVY61UpYQWcsuitHr/Eah5KLoVyTZjCRMDhZsyXcD/fh3SVJ/Xk1pTQlBg324dkzSrsCnmtS1hVHnnG0bFyLZZ/chI+MKSIwcZSl66Xv1+PbGm6NoUFGMLO6ZbUZAiFv/+4kqO2wd7uFEnDxFJF2NTQeby3YWVyZLFPWgxIIZVpQ+N1ClciYoCOB7rJcA4Xnb4BRrLe9fRm+iDlfn8sP6VwE+Y0+dfOf+Ocodm8w9qYIwCsHi/bzL1MSeZbrOkRVvbB8pmADx7ovfc+EbqrALqNy3LIM/w=; _sm=189d82e2edd67-000a09ba356d55-1a525634-1296000-189d82e2ede9af; meitustat={%22wgid%22:%22189d82e2edd67-000a09ba356d55-1a525634-1296000-189d82e2ede9af%22}; sso_access_token=A/IowePAUxo+Q3beJiqz7VY5Mv4rMtPl0MhvohuEzAIGnLAkG+HBOwtk7IhB75csQh4Rav1oVf2o0B0pi3PMUHDGlW9KRBOlGCtAc6lBB7r+EmFERXZ6gysw5a4Gfxv40wkv4ANvdjs8xxEQjx8kYQ==' \
  -H 'Origin: https://lingwen.tatstm.com' \
  -H 'Referer: https://lingwen.tatstm.com/dashboard/zlfx/jczl/bkfx/detail/c2lnbmFsIDYgKFNJR0FCUlQpLGNvZGUgLTYgKFNJX1RLSUxMKQovYXBleC9jb20uYW5kcm9pZC5ydW50aW1lL2xpYjY0L2Jpb25pYy9saWJjLnNvKGFib3J0KQ==?metricId=114&partitionOffset=0_541196099_df_2_&projectId=141&appVersions%5B0%5D=-1&modules%5B0%5D=-1&crashType%5B0%5D=native&crashErrorType=&time%5B0%5D=day&time%5B1%5D=1704038400&time%5B2%5D=1706630399&time%5B3%5D=&brand%5B0%5D=-1&models%5B0%5D=-1&channel%5B0%5D=-1&osVersions%5B0%5D=-1&stages%5B0%5D=-1&gid=&functionSymbol=&identity%5B0%5D=-1&platform=android' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
  -H 'X-Dataworks-OwnerUid: 4775' \
  -H 'X-Dataworks-ProjectIds: [\"85\"]' \
  -H 'X-Dataworks-RoleId: 5201' \
  -H 'X-Dataworks-RoleType: 20' \
  -H 'sec-ch-ua: \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  --data-raw '{\"projectNames\":[\"whee\"],\"projectName\":\"whee\",\"startTime\":\"1704038400\",\"endTime\":\"1706630399\",\"timeType\":4,\"aggregationType\":\"\",\"projectIds\":[141],\"crashType\":[\"native\"],\"platform\":\"android\",\"pageName\":\"bklb\",\"methodName\":\"signal 6 (SIGABRT),code -6 (SI_TKILL)\\n/apex/com.android.runtime/lib64/bionic/libc.so(abort)\"}' \
  --compressed"


def execCmd(cmd):
    # 获取输出的内容
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


def isMiniStatics(event, startTime, endTime):
    eventTime = int(event['time'])
    isInTime = int(startTime) <= eventTime & eventTime <= int(endTime)
    return ("mini_app_id" in event['params']) & isInTime

# 上报到后台的数据有两种格式, 需要分别匹配
def findPageName(params):
    if params.startswith('{'):
        pageNamePattern = r'(?<=page_name=).+(?=})'
    else:
        pageNamePattern = r'(?<=page_name\s).+'

    return re.findall(pageNamePattern, params)

#格式化时间
def strftime(timestone):
    # localtime只能接受10位时间戳,需要将13位时间戳转换为10位
    timeArray = time.localtime(float(timestone)/ 1000)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

# 服务器是以服务端接收埋点的时间来检索，不是客户端的埋点时间,
# 所以请求的时间跨度要长一点
def queryPageName(gid, startTime, endTime, reqStartTime, reqEndTime):
    reponds = execCmd(getCmd(gid, reqStartTime, reqEndTime))
    jsonRps = json.loads(reponds)

    pageName = "没有response"
    print("find pre, gid:" + gid + ",startTime:" + strftime(startTime) + ",endTime:"+ strftime(endTime))
    for event in jsonRps['response']:
        print("event:", event)
        if isMiniStatics(event, startTime, endTime):
            regMatch = findPageName(event['params'])
            if len(regMatch) > 0:
                pageName = regMatch[0]
            else:
                pageName = "response没有小程序埋点"


    return pageName


crashListResponds = execCmd(crashListCmd)
crashList = json.loads(crashListResponds)
result = {}
count = 0
for crash in crashList['response']:
    count = count + 1
    crashTime = crash['crashTime']
    gid = crash['gid']
    startTime = crashTime - 10 * 1000
    endTime = crashTime
    reqStartTime = crashTime - 60 * 1000
    reqEndTime = crashTime + 60 * 1000
    pageName = queryPageName(gid, str(reqStartTime), str(reqEndTime), str(reqStartTime), str(reqEndTime))
    if pageName in result:
        result[pageName] = result[pageName] + 1
    else:
        result[pageName] = 1
    print("crashList" + str(count) + ",map:",result)

# print("crashList" + str(count) + ",map:" + result)
