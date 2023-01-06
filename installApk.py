# coding=utf-8

import os

# os.system不支持读取, 会直接输出控制台
# os.system('adb devices')
# os.popen支持读取
ct = os.popen('adb devices').read()
ctArr = ct.split("\n")
deviceArr = []
currentDeviceIndex = 0
for ele in ctArr:
    if ele.endswith('device') == False:
        continue

    deviceArr.append(ele.split("\tdevice")[0])

print("可选择的设备:" + str(deviceArr))
# python 2.x中input如果需要接收str类型，必须输入时带"", 否则会报错
# raw_input会将所有输入都当做字符串, 不需要输入时带""
# python 3中input才变成默认接收str类型
print("功能介绍:\n")
print("\t1.退出:esc\n")
print("\t2.选择要安装的Device序号:index\n")
print("\t3.安装APK:任意输入\n")
while 1:
    commond = input('>>>')

    if commond == 'esc':
        break
    if commond == 'index':
        indexCom = input('\t>>>选择要安装的Device序号\n')
        currentDeviceIndex = int(indexCom)
    else:
        iCom = input('\t>>>输入安装APK命令(省略adb -s前缀)\n')
        print('adb -s ' + deviceArr[currentDeviceIndex] + ' ' + iCom)
        os.system('adb -s ' + deviceArr[currentDeviceIndex] + ' ' + iCom)
