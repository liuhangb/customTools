# coding=utf-8
#清理mac电脑上的代码缓存文件, 释放空间

import os

from pathlib import Path
import shutil


# 使用PathLib计算文件夹大小
def get_directory_size(directory):
    path = Path(directory)
    total_size = sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())
    return total_size

# 使用PathLib库统计各文件夹大小
def countDirSize(dirList):
    for i in range(0, len(dirList)):
        path = os.path.join(baseDir, dirList[i])
        size = get_directory_size(path)
        sizeMB = int(size / 1024 / 1024)
        print("path:%s, size:%d MB"%(path, sizeMB))

# 判断文件夹是否需要忽略;
# 隐藏文件夹直接忽略不清理
def isNeedIgnore(dirName):
    return dirName.startswith(".")

# 判断是否是build文件夹
def isBuildDir(dirPath):
    return dirPath.endswith("build")

#寻找build文件夹
def findBuildDir(dirPath, nextDirList):
    if os.path.isdir(dirPath):
        list = os.listdir(dirPath)
        for i in range(0, len(list)):
            if isNeedIgnore(list[i]):
                continue
            path = os.path.join(dirPath, list[i])
            # print("path:%s"%path)
            if os.path.isdir(path):
                if isBuildDir(path):
                    return path
                else:
                    nextDirList.append(path)
                    # print(nextDirList)
        return ""
    else:
        return ""

#使用shutil库删除文件夹
def deleteDir(dirPath):
    # 检查文件夹是否存在
    if os.path.exists(dirPath):
        # 删除文件夹
        shutil.rmtree(dirPath)
        print(f"The folder '{dirPath}' has been deleted.")
    else:
        print(f"The folder '{dirPath}' does not exist.")

# 删除code build文件夹
def cleanCodeBuild(dirList):
    for i in range(0, len(dirList)):
        count = 4
        currentDirList = [dirList[i]]
        # 最多遍历四层目录
        while count > 0:
            if len(currentDirList) == 0:
                break
            count -= 1
            nextDirList = []
            for j in range(0, len(currentDirList)):
                buildPath = findBuildDir(currentDirList[j], nextDirList)
                if isBuildDir(buildPath):
                    print("delete path:%s"%buildPath)
                    deleteDir(buildPath)

            currentDirList = nextDirList
            print(currentDirList)







baseDir = "/Users/liuhang/sourcecode/Android"
list = os.listdir(baseDir)


dirList = []
for i in range(0, len(list)):
    path = os.path.join(baseDir, list[i])
    if os.path.isdir(path):
        dirList.append(path)
#countDirSize(dirList)
print("待清理目录:", dirList)
cleanCodeBuild(dirList)
print("清理后=====================")
countDirSize(dirList)




