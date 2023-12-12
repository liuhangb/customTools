# coding=utf-8

import os
import re
import sys
import getopt


def showHint(deviceArr):
    print("可选择的设备:" + str(deviceArr))
    print("功能介绍:\n")
    print("\t😈 选择要安装的Device序号:-x\n")
    print("\t😈 安装应用前先卸载应用:-d\n")
    print("\t😈 apk路径:-i\n")


def queryDevices():
    # os.system不支持读取, 会直接输出控制台
    # os.system('adb devices')
    # os.popen支持读取
    ct = os.popen('adb devices').read()
    ctArr = ct.split("\n")
    deviceArr = []
    for ele in ctArr:
        if ele.endswith('device') == False:
            continue

        deviceArr.append(ele.split("\tdevice")[0])
    return deviceArr


def checkParam():
    if apkPath == '':
        exit("apkPath 不能为空")


argv = sys.argv[1:]
opts, args = getopt.getopt(argv, "x:i:d")  # 短选项模式
currentDeviceIndex = 0
apkPath = ''
isFirstDelete = False
deviceArr = queryDevices()

if not opts:
    showHint(deviceArr)
    exit()
# python 2.x中input如果需要接收str类型，必须输入时带"", 否则会报错
# raw_input会将所有输入都当做字符串, 不需要输入时带""
# python 3中input才变成默认接收str类型
for opt, arg in opts:
    if opt in ['-x']:
        currentDeviceIndex = arg
    elif opt in ['-i']:
        apkPath = arg
    elif opt in ['-d']:
        isFirstDelete = True
    else:
        exit("未支持的参数:"+opt)

checkParam()

command = "adb -s " + deviceArr[currentDeviceIndex]
if isFirstDelete:
    # 先卸载
    queryPkgCmd = "/Users/liuhang/Library/Android/sdk/build-tools/33.0.0/aapt2 dump badging " + apkPath
    apkInfo = os.popen(queryPkgCmd)
    packageName = re.findall(r"package: name=\'(.+?)\'", apkInfo.read())[0]
    os.system(command + " uninstall " + packageName)

os.system(command + " install " + apkPath)
